import pymongo
import os


def print_hi(name):
    print(f'Hi, {name}')


# Connect to MongoDB
client = pymongo.MongoClient(os.environ['MONGODB_URI'])
db = client.myFirstDatabase
countries = db.countries
continents = db.continents


def dbTable():
    print ("{:<8} {:<15} {:<10} {:<10}".format('Name', 'Continent', 'Population', 'id'))
    for country in countries.find():
        print("{:<8} {:<15} {:<10} {:<10}".format(str(country['name']), str(country['continent']), str(country['population']), str(country['_id'])))


# Number 1: searches a substring in countries names
def searchCountry(substring):
    for country in countries.find({'name': {'$regex': substring, '$options': 'i'}}):
        print(country['name'])

# Number 2: adds a continent collection reference to countries
def contToCountries():
    for country in countries.find():
        continent = continents.find_one({'_id': country['_id']})
        countries.update_one({'_id': country['_id']}, {'$set': {'continent': continent}})


# Number 3: Print the list of continents with their first 3 countries
def contsWithCountries():
    for continent in continents.find():
        print(continent)
        if f'{continent["name"]}' != 'Europe':
            for country in continent['countries']:
                # print(country)
                print(countries.find_one({'_id': country})['name'])


# Number 4: Gets till the 4th country under specified continent ordered by name
def upTo4th():
    for continent in continents.find():
        print(continent['name'])
        for country in continent['countries'][:4]:
            print(countries.find_one({'_id': country}))


# Number 5: Adds population field to countries
def popToCountries():
    for country in countries.find():
        countries.update_one({'_id': country['_id']}, {'$set': {'population': country['population']}})
        print(country['population'])


# Number 6: Gets all countries ordered by population in ascending order
def orderedByPopulation():
    for country in countries.find().sort('population', pymongo.ASCENDING):
        print(str(country['name'] + ' ' + str(country['population'])))


# Number 7: Gets countries where population is greater than 100000 and including u in the country name
def greater100000():
    for country in countries.find({'population': {'$gt': 100000}, 'name': {'$regex': 'u', '$options': 'i'}}):
        print(country['name'])


if __name__ == '__main__':
    print_hi('IntelliJ Rocks!')
    dbTable()
    # searchCountry('neth')  # Number 1
    # contToCountries()  # Number 2
    # contsWithCountries()  # Number 3
    # upTo4th()  # Number 4
    # popToCountries()  # Number 5
    # orderedByPopulation()  # Number 6
    # greater100000()  # Number 7
