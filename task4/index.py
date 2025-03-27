import argparse
import csv
from pathlib import Path
from collections import defaultdict
import math

def read_documents(docs_dir):
    documents = {}
    
    for doc_path in Path(docs_dir).glob('*'):
        with open(doc_path, 'r', encoding='utf-8') as f:
            terms = f.read().split()
            doc_id = doc_path.stem
            documents[doc_id] = terms
    return documents

def calculate_tf(documents):
    tf = defaultdict(dict)
    for doc_id, terms in documents.items():
        term_count = defaultdict(int)
        for term in terms:
            term_count[term] += 1
        
        total = len(terms)
        for term, count in term_count.items():
            tf[doc_id][term] = count / total
    return tf

def calculate_idf(documents):
    doc_count = defaultdict(int)
    
    for terms in documents.values():
        for term in set(terms):
            doc_count[term] += 1
    
    idf = {}
    total_docs = len(documents)
    for term, count in doc_count.items():
        idf[term] = math.log(total_docs / count)
    return idf

def calculate_tfidf(tf, idf):
    tfidf = defaultdict(dict)
    for doc_id, terms in tf.items():
        for term, tf_value in terms.items():
            tfidf[doc_id][term] = tf_value * idf.get(term, 0)
    return tfidf

def save_csv(data, filename, value_name):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['document', 'term', value_name])

        sorted_docs = sorted(data.items(), key=lambda x: int(x[0]))
        
        for doc_id, terms in sorted_docs:
            sorted_terms = sorted(terms.items(), key=lambda x: x[0])
            for term, value in sorted_terms:
                writer.writerow([doc_id, term, round(value, 6)])

def save_idf_csv(idf, filename):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['term', 'idf'])
        for term, value in sorted(idf.items(), key=lambda x: x[0]):
            writer.writerow([term, round(value, 6)])

def main(docs_dir):
    documents = read_documents(docs_dir)

    tf = calculate_tf(documents)
    idf = calculate_idf(documents)
    tfidf = calculate_tfidf(tf, idf)

    save_csv(tf, 'tf.csv', 'tf')
    save_idf_csv(idf, 'idf.csv')
    save_csv(tfidf, 'tfidf.csv', 'tf-idf')
    
    print("Files saved:")
    print("- tf.csv (Term Frequencies)")
    print("- idf.csv (Inverse Document Frequencies)")
    print("- tfidf.csv (TF-IDF scores)")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TF-IDF Calculator')
    parser.add_argument('docs_dir', help='Path to processed documents directory')
    args = parser.parse_args()

    main(docs_dir=args.docs_dir)
