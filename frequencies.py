"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    
    list_one = []
    list_two = []
    
    list_one.append(items[0])
    items.remove(items[0])
    for item in items:
        if item in list_one:
            list_one.append(item)
        else:
            list_two.append(item)

    frequencies[list_one[0]] = len(list_one)
    frequencies[list_two[0]] = len(list_two)

       
    return frequencies

if __name__ == "__main__":
    item_list = ["banana", "apple", "apple", "banana"]
    print(frequencies(item_list))

