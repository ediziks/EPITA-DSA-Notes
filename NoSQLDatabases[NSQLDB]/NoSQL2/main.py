import pymongo
import os


def print_hi(name):
    print(f'Hi, {name}')


def connectDB():
    client = pymongo.MongoClient(os.environ['MONGO_URL'])
    db = client.myFirstDatabase
    print(db.list_collection_names())

    countries = db.countries
    continents = db.continents

    for country in countries.find():
        print(country['name'])


if __name__ == '__main__':
    print_hi('IntelliJIDEA')
    connectDB()
































