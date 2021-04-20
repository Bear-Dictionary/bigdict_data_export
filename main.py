from csv_writer import CsvWriter
from export_dictionary import export_dictionary
from pymongo import MongoClient

if __name__ == '__main__':
    name = "Từ điển Nga Việt tổng hợp"
    target = name + '.csv'

    client = MongoClient("mongodb://root:root@localhost:27017")
    csvWriter = CsvWriter(target)


    def writer(word, fromLang, toLang, content):
        csvWriter.write(word, fromLang, toLang, content)


    export_dictionary(client=client, name=name, writer=writer)
