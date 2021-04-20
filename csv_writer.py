import csv


class CsvWriter:
    def __init__(self, filename):
        self.csv = open(filename, 'w', newline='')
        self.writer = csv.writer(self.csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    def write(self, word, fromLang, toLang, content):
        self.writer.writerow([word,fromLang, toLang, content])
