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
    # route = [None] * length
    route = []

    """
    YOUR CODE HERE
    """

    # ? fill table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # ? initialize destination as none (ie first destination)
    destination = hash_table_retrieve(hashtable, 'NONE')

    while destination != 'NONE':
        route.append(destination)
        # ? change value of destination until it == none again (ie last destination)
        destination = hash_table_retrieve(hashtable, destination)
        # print(f'dest ==> {destination}')

    # print(f'route ==> {route}')
    return route


# tickets = [
#     Ticket("PIT", "ORD"),
#     Ticket("XNA", "SAP"),
#     Ticket("SFO", "BHM"),
#     Ticket("FLG", "XNA"),
#     Ticket("NONE", "LAX"),
#     Ticket("LAX", "SFO"),
#     Ticket("SAP", "SLC"),
#     Ticket("ORD", "NONE"),
#     Ticket("SLC", "PIT"),
#     Ticket("BHM", "FLG"),
# ]

# reconstruct_trip(tickets, 10)
