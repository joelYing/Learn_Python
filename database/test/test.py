import pymongo


def x():
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db['second']

    with open('D:\\mygit\\learn_python\\Learn_Python\\domain.txt', 'r') as fw:
        for index, line in enumerate(fw.readlines()):
            domain = line.strip()
            result_one = collection.insert_one({'_id': index, 'domain': domain})
            print(result_one.inserted_id)


if __name__ == '__main__':
    x()