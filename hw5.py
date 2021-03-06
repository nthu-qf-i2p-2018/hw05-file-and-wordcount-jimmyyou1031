import csv
import json
import pickle
import string

def main(filename):
    txtfile = open(filename)
    lines = txtfile.readlines()
    all_words = []
    for line in lines:
        line = line.strip()
        words = line.split()
        for word in words:
            word = word.strip(string.punctuation)
            if word != ("" ""):
                all_words.append(word)
    from collections import Counter
    counter = Counter()
    counter.update(all_words)

    with open("wordcount.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(['word', 'count'])
        for f in set(all_words):
            writer.writerow([f,all_words.count(f)])
    with open("wordcount.json", "w") as json_file:
        json.dump(counter, json_file)
    with open("wordcount.pkl", "wb") as pkl_file:
        pickle.dump(counter, pkl_file)

if __name__ == '__main__':
    main("i_have_a_dream.txt")
