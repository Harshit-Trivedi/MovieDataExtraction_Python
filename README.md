# Overview
For movie data extraction, I have used Python to access movie data. I have imported the omdb package. Next, I set up the omdb API to be used to pull movie data.
Finally, I used the search() method to extract movie data. For the target keywords, I have extracted title, imdb ID, year of release & movie type. Here, I have set to 
calls limit to 20, since it allowed only a limited of API calls per day. The page count can be extended upto 100.

## Movie API source
http://www.omdbapi.com/

## Target Keywords

“Canada”, “University”, “Moncton”, “Halifax”, “Toronto”, “Vancouver”, “Alberta”, “Niagara”.

## File description

* movie_extraction.py: This python script file has the code for API setup, movie data extraction for title, imdb ID, year of release & movie type and data cleaning 
process.

* movie_extraction_pt2.py: Script to extract movie rating, genre, and plot from the stored movie data.

* movie_data_cleaned.json: 

## Data Cleaning

For all the movie data, I have removed emoticons, symbols, pictographs, transport/map symbols, flags(iOS), special characters and tags. For removing the special 
characters, I have used regex substitution. For cleaning all the emojis, symbols, etc. I have created a separate custom function named “clean_emoji”. This function also 
performs a regex operation to substitute and clean data.
