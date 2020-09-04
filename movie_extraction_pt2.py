import omdb
import re

# set up OMDB API to be used to pull data
client = omdb.OMDBClient(apikey='5203b3e3')

# code logic similar to movie extraction code

# search keywords
words = ['Canada', 'University', 'Moncton', 'Halifax', 'Toronto', 'Vancouver''Alberta', 'Niagara']
data = []   # empty list to which movie_details obj will be added
print ("Searching for movie data...")

# API call from http://www.omdbapi.com/
for z in range(1, 20):
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
            data.append(movie_details)
            continue
        else:
            pass
print ("Fetching and cleaning data...")

collection = []
for entry in data:
    for x in entry:
        collection.append(client.get(title=x[0]))
print(collection)
