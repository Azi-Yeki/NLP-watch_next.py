# import spacy
# load en_core_web
import spacy
nlp = spacy.load('en_core_web_md')

# open the file for reading
file = open("movies.txt", "r")
movies = file.readlines()

movie_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Define the function with its parameter.
def watch_next(description):
    nlp_description = nlp(description)

    # Create at empty list to store the similarities
    similar = []

    # finding the similarities and appending them to the empty list that was created
    for movie in movies:
        similarity = nlp(movie).similarity(nlp_description)
        similar.append(similarity)

    # use max to find the movie with the highest similarity
    highest = max(similar)
    most_similar = movies[similar.index(highest)]
    return most_similar

# Print the movie that the user should watch next using watch_next() function we defined
print(f'You should watch this next: {watch_next(movie_to_compare)}')