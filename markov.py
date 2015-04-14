import sys


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    markov_dict = {}

    corpus = open(corpus)

    corpus_list = []

    for line in corpus:
        line = line.rstrip().split(" ") # extracting all words into lists
        corpus_list.extend(line) # add lines to the corpus_list to create one big list of words

    print corpus_list

    corpus_line = range(len(corpus_list) - 2)

    for i in corpus_line:

        if (corpus_list[i], corpus_list[i + 1]) in markov_dict:  # if this key exists, add the dict[key] = value
            markov_dict[(corpus_list[i], corpus_list[i + 1])] = markov_dict.get((corpus_list[i], corpus_list[i + 1])) + [corpus_list[i + 2]] # constructing list of trailing words

        else: # if this key does not exist, create key and value
            markov_dict[(corpus_list[i], corpus_list[i + 1])] = [corpus_list[i + 2]]
    


    """
    Our pseudocode, first thoughts:

    first get length of each list 

    corpus_line = range(len(line)) == 0 - 7
    for i in corpus_line:
        line[i] = first word in tuple #1
        line[i + 1] = second word in tuple #1
        i = i + 1


    then take list[0], list[1] = tuple
    then add one to each index until reach the end of list
    list[1], list[2] and so on...

    for each tuple
        take the two words and create a tuple 
        then we need to count frequency of each tuple (using word count exercise logic)
        return keys into markov_dict
        markov_dict[tuple] = value is all immediately trailing words

    Notes:
    - We learned how to make tuples simply by syntax ()
    - Without this knowledge, we thought there were many more steps!

    """


    return markov_dict


# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     return "Here's some random text."


# # Change this to read input_text from a file, deciding which file should
# # be used by examining the `sys.argv` arguments (if neccessary, see the
# # Python docs for sys.argv)

# # import fileinput
# # for line in fileinput.input():
# #     process(line)

input_text = "green-eggs.txt"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

print make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text
