import csv
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

def load_sentences_from_csv(file_path):
    sentences = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row:
                sentence = row[0]
                sentences.append(sentence)
    return sentences

def find_most_common_parts(sentences):
    # Tokenizacja i zliczanie części zdań
    parts = []
    for sentence in sentences:
        tokenized_sentence = word_tokenize(sentence)
        parts.extend(tokenized_sentence)

    # Znajdowanie najczęściej występujących części
    common_parts = Counter(parts).most_common()

    # Wyświetlanie najczęściej występujących części
    print("Najczęściej występujące części zdań:")
    for part, count in common_parts:
        print(f"{part}: {count} razy")

# Wczytanie danych z pliku CSV
csv_file_path = 'C:\\Programowanie\\PYTHON\\DATAANALYSIS\\pododnezdania\\podobne.csv'
sentences = load_sentences_from_csv(csv_file_path)

# Znajdowanie najczęściej występujących części zdania
find_most_common_parts(sentences)