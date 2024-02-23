# fuzzy_search word guesser

## Outline
Input should be a list of queries or text about the desired topic.
For example: a list of queries history-inputs into a search bar of a wine retail company's online shop.
The algorithm 'learns' from that input and makes in the first step of
1. Create a target list of words from the input data which consists
of all words which an input should be matched to, aka the list where
a potential input is matched to.
For this target list all eligible words will be selected from the data input.
2. Create a count dictionary of all the words and their counts, this dictionary
is used for getting the most popular match to a single word
3. Create a co-occurence dict of words that includes the top words that appear
with each word in the input data
4. Construct a get closest match function for the cases
of single words or sentences being input into the search bar
which uses Levenshtein-Distance and combines the ranking of it with the popularity and/or the co-occurence data previously created for this purpose.  
This way it is feasible to get a more 'intelligent' level of matching to the closest possible match

