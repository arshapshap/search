import argparse
import re
from pathlib import Path
from pymorphy3 import MorphAnalyzer

def load_index(index_file):
    index = {}
    with open(index_file, 'r', encoding='utf-8') as f:
        for line in f:
            doc_id, url = line.strip().split('\t')
            index[doc_id] = url
    return index

def build_inverted_index(docs_dir):
    inverted_index = {}
    all_docs = set()

    for doc_path in Path(docs_dir).glob('*.txt'):
        doc_id = doc_path.stem
        all_docs.add(doc_id)

        with open(doc_path, 'r', encoding='utf-8') as f:
            terms = f.read().split()
            for term in set(terms):
                inverted_index.setdefault(term, set()).add(doc_id)

    return inverted_index, all_docs

def save_inverted_index(index, filename='inverted_index.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        for term in sorted(index.keys()):
            docs = ' '.join(sorted(index[term]))
            f.write(f"{term}\t{docs}\n")

def lemmatize_term(term, morph):
    return morph.parse(term)[0].normal_form

def tokenize_query(query):
    query = re.sub(r'([&|!()])', r' \1 ', query)
    return re.findall(r'\b\w+\b|[&|!()]', query)

def parse_query(tokens, morph):
    output = []
    stack = []
    precedence = {'!': 3, '&': 2, '|': 1}

    for token in tokens:
        if token in precedence:
            while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            output.append(lemmatize_term(token.lower(), morph))

    while stack:
        output.append(stack.pop())

    return output

def evaluate_postfix(postfix, inverted_index, all_docs):
    stack = []
    for token in postfix:
        if token == '&':
            b, a = stack.pop(), stack.pop()
            stack.append(a & b)
        elif token == '|':
            b, a = stack.pop(), stack.pop()
            stack.append(a | b)
        elif token == '!':
            a = stack.pop()
            stack.append(all_docs - a)
        else:
            stack.append(inverted_index.get(token, set()))
    return stack.pop() if stack else set()

def search(query, inverted_index, all_docs, morph):
    tokens = tokenize_query(query)
    postfix = parse_query(tokens, morph)
    result = evaluate_postfix(postfix, inverted_index, all_docs)
    return sorted(result, key=lambda x: int(x))

def main(docs_dir, index_file):
    morph = MorphAnalyzer()
    index = load_index(index_file)
    inverted_index, all_docs = build_inverted_index(docs_dir)
    save_inverted_index(inverted_index)

    print("Inverted index saved to inverted_index.txt")
    print("\nQuery examples:")
    print("apple & banana | !orange")
    print("(apple | banana) & !orange")
    print("apple & banana | orange")

    while True:
        try:
            query = input("\nEnter query (or 'exit' to quit): ").strip()
            if query.lower() == 'exit':
                break

            results = search(query, inverted_index, all_docs, morph)
            if results:
                print(f"Found documents:")
                print(f"{'-' * 20}")
                print(f"doc_id\turl")
                print('\n'.join([f"{doc_id}\t{index[doc_id]}" for doc_id in results]))
                print(f"{'-' * 20}")
                print(f"Total: {len(results)} documents.")
            else:
                print("No documents found")

        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Boolean search engine')
    parser.add_argument('docs_dir', help='Path to processed documents directory')
    parser.add_argument('index_file', help='Path to index with URLs')
    args = parser.parse_args()

    main(docs_dir=args.docs_dir, index_file=args.index_file)
