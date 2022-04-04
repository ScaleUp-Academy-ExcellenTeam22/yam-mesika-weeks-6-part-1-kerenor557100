#submitted by Keren Or Hadad 208025205
import string

def count_words(my_string):
    """

    :param my_string: given text
    :return: returns a dictionary of the texts word lengths
    """
    my_string = my_string.lower().split()
    sample_dictionary = {}
    for word in my_string:
        words = len(word)
        sample_dictionary[words] = word
    return sample_dictionary


print(count_words("hello everyone!"))
print(count_words("i love pizza"))

"""
output:
{5: 'hello', 9: 'everyone!'}
{1: 'i', 4: 'love', 5: 'pizza'}
"""

