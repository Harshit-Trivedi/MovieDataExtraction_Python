import re
import omdb
import pymongo as py

# setup db and collection for MongoDB
my_client = py.MongoClient('mongodb://127.0.0.1:27017/')
my_db = my_client['Asgmt3']
my_collection = my_db['movie']

# set up OMDB API to be used to pull data
client = omdb.OMDBClient(apikey='5203b3e3')

# search keywords
words = ['Canada', 'University', 'Moncton', 'Halifax', 'Toronto', 'Vancouver''Alberta', 'Niagara']
data = []   # empty list to which movie_details obj will be added
print ("Searching for movie data...")

# API call from http://www.omdbapi.com/
for z in range(1, 90):
    for word in words:
        movies = client.search(word, page=z)
        for movie in movies:
            movie_details = {
                'title': movie['title'], 'poster': movie['poster'],
                'imdb ID': movie['imdb_id'], 'year': movie['year'],
                'type': movie['type']
            }
            data.append(movie_details)

        # special tags regex reference: https://www.webdeveloper.com/d/199621-need-a-regex-to-exclude-all-but-a-za-z0-9s
        if movie_details['type'] is not None:
            movie_details['type'] = re.sub(r'[^a-zA-Z0-9\s\.]+', '', movie_details['type'])

        # skipping pages that are empty and have no data
        if movies == []:
            continue
        else:
            pass
print ("Data cleaning finished")

# sending data to mongoDB
my_collection.insert_many(data)
print('Data stored successfully in MongoDB')
