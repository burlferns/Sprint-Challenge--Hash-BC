#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for elem in tickets:
        hash_table_insert(hashtable, elem.source, elem.destination)

    value = hash_table_retrieve(hashtable, "NONE")
    index = 0
    while (value != "NONE"):
        route[index]=value
        value = hash_table_retrieve(hashtable, value)
        index += 1

    route.pop()

    return route
    
