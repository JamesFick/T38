'''
Read in the movies.txt file. Each separate line is a description of a different
movie.
● Your task is to create a function to return which movies a user would watch
next if they have watched Planet Hulk with the description “Will he save their world or destroy it?
When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to
a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery
and trained as a gladiator.”
● The function should take in the description as a parameter and return the title of the most similar movie.
● Host your solution on a Git host such as GitLab or GitHub.
○ Remember to exclude any venv or virtualenv files from your repo.
● Add the link for your remote Git repo to your semantic_similarity.txt file
'''
import spacy
nlp = spacy.load('en_core_web_md')

planet_hulk = '''Will he save their world or destroy it?
When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to 
a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery
and trained as a gladiator.'''

# Create a dictionary to store movies and their descriptions.
films = {}
with open('movies.txt', 'r') as movies:
    for line in movies:
        line = line.strip()
        key = line[:8]
        value = line[9:]
        films[key] = value


# The function should take in the description as a parameter and return the title of the most similar movie
token = nlp(planet_hulk)
highest_sim = 0
name = None
for film_name, value in films.items():
    tok = nlp(value)
    print(f'The similarity between \'Planet Hulk\' and {film_name} is: {token.similarity(tok)}')
    similarity = token.similarity(tok)
    if similarity > highest_sim:
        highest_sim = similarity
        name = film_name

# Return results.
print(f"\nThe movie with the highest similarity to 'Planet Hulk' is: {name}")

