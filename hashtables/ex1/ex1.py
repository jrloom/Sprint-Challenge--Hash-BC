#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    # ? fill table
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)

    # ? find low values
    for low in range(len(weights)):
        # ? higher value == weight limit - lower value
        high = hash_table_retrieve(ht, (limit - weights[low]))
        # ? check if high is None (None > int == error)
        if high:
            if high > low:
                # ? yes...these are indices, not the values of the indices...
                print(high, low)
                return [high, low]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
