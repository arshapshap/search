import argparse
import re
from pathlib import Path
from pymorphy3 import MorphAnalyzer

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

def save_index(index, filename='inverted_index.txt'):
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

def evaluate_postfix(postfix, index, all_docs):
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
            stack.append(index.get(token, set()))
    return stack.pop() if stack else set()

def search(query, index, all_docs, morph):
    tokens = tokenize_query(query)
    postfix = parse_query(tokens, morph)
    result = evaluate_postfix(postfix, index, all_docs)
    return sorted(result)

def main(docs_dir):
    morph = MorphAnalyzer()
    index, all_docs = build_inverted_index(docs_dir)
    save_index(index)

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

            results = search(query, index, all_docs, morph)
            if results:
                print(f"Found {len(results)} documents:")
                print(" ".join(results))
            else:
                print("No documents found")

        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Boolean Search Engine')
    parser.add_argument('docs_dir', help='Path to processed documents directory')
    args = parser.parse_args()

    main(docs_dir=args.docs_dir)
