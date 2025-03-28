import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path
from pymorphy3 import MorphAnalyzer

def load_index(index_file):
    index = {}
    with open(index_file, 'r', encoding='utf-8') as f:
        for line in f:
            doc_id, url = line.strip().split('\t')
            index[doc_id] = url
    return index

def load_tfidf(tfidf_file):
    tfidf = defaultdict(dict)
    with open(tfidf_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            doc_id = row['document']
            term = row['term']
            score = float(row['tf-idf'])
            tfidf[doc_id][term] = score
    return tfidf

def load_idf(idf_file):
    idf = {}
    with open(idf_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            idf[row['term']] = float(row['idf'])
    return idf

def process_query(query, morph, idf):
    tokens = query.lower().split()
    lemmas = [morph.parse(token)[0].normal_form for token in tokens]

    term_counts = defaultdict(int)
    total_terms = len(lemmas)
    for lemma in lemmas:
        term_counts[lemma] += 1

    query_vec = {}
    for lemma, count in term_counts.items():
        if lemma in idf:
            tf = count / total_terms
            query_vec[lemma] = tf * idf[lemma]

    return query_vec

def cosine_similarity(query_vec, doc_vec):
    dot_product = sum(query_vec[term] * doc_vec.get(term, 0) for term in query_vec)
    query_norm = math.sqrt(sum(v**2 for v in query_vec.values()))
    doc_norm = math.sqrt(sum(v**2 for v in doc_vec.values()))

    if query_norm == 0 or doc_norm == 0:
        return 0
    return dot_product / (query_norm * doc_norm)

def search(query, tfidf, idf, morph):
    query_vec = process_query(query, morph, idf)
    if not query_vec:
        return []

    scores = []
    for doc_id, doc_vec in tfidf.items():
        score = cosine_similarity(query_vec, doc_vec)
        if (score > 0):
            scores.append((doc_id, score))

    return sorted(scores, key=lambda x: x[1], reverse=True)

def main(csv_dir, index_file):
    morph = MorphAnalyzer()

    index = load_index(index_file)
    tfidf = load_tfidf(Path(csv_dir) / 'tfidf.csv')
    idf = load_idf(Path(csv_dir) / 'idf.csv')

    print("Vector search engine ready")

    while True:
        try:
            query = input("\nSearch query (or 'exit'): ").strip()
            if query.lower() == 'exit':
                break

            results = search(query, tfidf, idf, morph)
            if results:
                print(f"{'-' * 20}")
                print("score\tdoc_id\turl")
                for doc_id, score in results:
                    print(f"{score:.4f}\t{doc_id}\t{index[doc_id]}")
                print(f"{'-' * 20}")
                print(f"Total: {len(results)} documents.")
            else:
                print("No documents found")

        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Vector search engine')
    parser.add_argument('csv_dir', help='Path to directory with csv')
    parser.add_argument('index_file', help='Path to index with URLs')
    args = parser.parse_args()

    main(csv_dir=args.csv_dir, index_file=args.index_file)
