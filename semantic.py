'''Follow these steps:
● Create a file called semantic.py and run all the code extracts above.
● Write a note about what you found interesting about the similarities
between cat, monkey and banana and think of an example of your own.
● Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on what you notice is different from the model
'en_core_web_md'.
● Host your solution on a Git host such as GitLab or GitHub.
○ Remember to exclude any venv or virtualenv files from your repo.
● Add the link for your remote Git repo to a text file named semantic_similarity.txt'''

# 1
import spacy

nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# 2
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Write a note about what you found interesting about the similarities
# between cat, monkey and banana
# - there is higher similarity between monkey and banana than a cat and any fruit.
# - there is high similarity between fruits
# think of an example of your own.

tokens = nlp('umbrella rain cupcake oven ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# - apparently similarity between umbrella and rain is low as well as with the cupcake and the oven.
# - cupcake correlates slightly stronger with oven.

# 3
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)


# Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on what you notice is
# different from the model 'en_core_web_md'.

import spacy

nlp = spacy.load('en_core_web_sm')

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Error messahe UserWarning: [W007] The model you're using has no word vectors loaded,
# so the result of the Token.similarity method will be based on the tagger, parser and NER,
# which may not give useful similarity judgements.
# This may happen if you're using one of the small models, e.g. `en_core_web_sm`,
# which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors,
# or use one of the larger models instead if available.
# print(token1.text, token2.text, token1.similarity(token2))

# Generally I observe higher similarity levels for cat and apple, even higher than with cat and monkey.
# apple with banana correlation is low, and banana and monkey is low as well. the results are different to those
# from the stronger model and seems to be irrational.
