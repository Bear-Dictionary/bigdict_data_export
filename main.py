from csv_writer import CsvWriter
from export_dictionary import export_dictionary
from pymongo import MongoClient
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tool for export data from Bigdict')
    parser.add_argument('dictionary', metavar='D', help='Dictionary name')
    parser.add_argument('--address', dest='address', help='MongoDB address',
                        default='mongodb://root:root@localhost:27017')
    parser.add_argument('--output', dest='output', help='Output file')

    args = parser.parse_args()
    mongoAddress = args.address
    name = args.dictionary
    output = args.output + '.csv'

    client = MongoClient(mongoAddress)
    csvWriter = CsvWriter(output)


    def writer(word: str, from_lang: str, to_lang: str, content: str):
        csvWriter.write(word, from_lang, to_lang, content)


    export_dictionary(client=client, name=name, writer=writer)
