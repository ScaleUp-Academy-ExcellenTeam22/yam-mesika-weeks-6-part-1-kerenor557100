#submitted by Keren Or Hadad 208025205

def be_hello(my_text):
    """
     The function receives text and returns to each word (including familiar characters) what its length is
    :param input: a text
    :return: returns a list of the length of the words in the text
    """
    input = input.split(" ")
    item = []
    for x in input:
        item.append(len(x))
    return item
"""
item
To add to the list that will be printed at the end
"""


print(be_hello("Toto, I've a feeling we're not in Kansas anymore"))
print(be_hello("i love you!"))

"""
output:
[5, 4, 1, 7, 5, 3, 2, 6, 7]
[1, 4, 4]
"""
