import sys

def make_chains(corpus1,corpus2):
    """Takes input text as string; returns dictionary of markov chains."""

    markov_dict = {}

    corpus1 = open(corpus1) 
    corpus2 = open(corpus2) 

    corpus_list = []

    for line in corpus1:
        line = line.rstrip().split(" ") # extracting all words into lists
        corpus_list.extend(line) # add lines to the corpus_list to create one big list of words

    for line in corpus2:
        line = line.rstrip().split(" ") # extracting all words into lists
        corpus_list.extend(line) # add lines to the corpus_list to create one big list of words

    corpus_line = range(len(corpus_list) - 2)

    for i in corpus_line:

        if (corpus_list[i], corpus_list[i + 1]) in markov_dict:  # if this key exists, add the dict[key] = value
            markov_dict[(corpus_list[i], corpus_list[i + 1])] = markov_dict.get((corpus_list[i], corpus_list[i + 1])) + [corpus_list[i + 2]] # constructing list of trailing words

        else: # if this key does not exist, create key and value
            markov_dict[(corpus_list[i], corpus_list[i + 1])] = [corpus_list[i + 2]]
    
    return markov_dict


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    new_string = ''

    first_item = chains.popitem() # pick an item from the dictionary at "random"

    k, v = first_item # unpack the key and value from the item

    new_string = k[0] + ' ' + k[1] # concatenating the words from the key tuple into a string

    next_tuple = (k[1], v.pop()) # create the next tuple by using the second word in the tuple and one word from the value

    while next_tuple in chains: # while the next tuple is included in the dictionary
        if next_tuple in chains.keys():
            new_value = chains[next_tuple] # sets the value of new_value if next_tuple exists in chains

            if new_value != []:
                new_value = new_value.pop() # sets new_value to random value of existing value list
                next_tuple = (next_tuple[1], new_value)
                new_string = new_string + ' ' + next_tuple[1]
            else:
                next_tuple = ()      
            
    return new_string


# This file uses sys to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# script,filename1 = sys.argv
script,filename1,filename2 = sys.argv

# input_text = filename

# Get a Markov chain
chain_dict = make_chains(filename1,filename2)

# Produce random text
random_text = make_text(chain_dict)

print random_text
