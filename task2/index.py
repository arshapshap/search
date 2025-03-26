import argparse
from pathlib import Path
import nltk
from razdel import tokenize
from pymorphy3 import MorphAnalyzer
from nltk.corpus import stopwords

def process_text(text, morph, russian_stopwords):
    tokens = [token.text.lower() for token in tokenize(text) if token.text.strip()]
    
    lemmas = []
    for token in tokens:
        lemma = morph.parse(token)[0].normal_form
        if lemma not in russian_stopwords and len(lemma) > 2:
            lemmas.append(lemma)
    
    return ' '.join(lemmas)

def process_documents(input_dir, output_dir):
    nltk.download('stopwords')

    morph = MorphAnalyzer()
    russian_stopwords = set(stopwords.words('russian'))

    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    processed_count = 0
    for file_path in input_path.glob("*"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()

            processed_text = process_text(text, morph, russian_stopwords)

            output_file = output_path / file_path.name
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(processed_text)

            processed_count += 1
            print(f'Processed: {file_path.name} -> {output_file.name}')

        except Exception as e:
            print(f'Error processing {file_path.name}: {e}')
    
    print(f'\nProcessing complete. Processed {processed_count} documents.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Text processing')
    parser.add_argument('input_dir', type=str, help='Path to directory with raw documents')
    args = parser.parse_args()

    process_documents(args.input_dir, 'docs')
