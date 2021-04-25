from typing import Callable
from pymongo import MongoClient


def export_dictionary(client: MongoClient, name: str, writer: Callable[[str, str, str, str], None]):
    dictionary = client.admin.dictionaries.find_one({'name': name})
    from_lang = client.admin.languages.find_one({'_id': dictionary['fromLang']})
    to_lang = client.admin.languages.find_one({'_id': dictionary['toLang']})
    words = client.admin.words.find({'meanings.dictionary': dictionary['_id']})

    print('Dictionary:', from_lang['code'], '->', to_lang['code'])
    count = 0
    for word in words:
        count += 1
        content = next((x for x in word['meanings'] if x['dictionary'] == dictionary["_id"]), None)
        writer(word['key'], from_lang['code'], to_lang['code'], content['htmlString'])

    print("Export:", count, "words")
