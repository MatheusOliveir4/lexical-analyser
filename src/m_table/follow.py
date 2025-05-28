from grammar import initial_variable
from m_table.m_table import first
from utils.find_head_production import find_head_productions
from utils.is_terminal import is_terminal

follow = {}

def make_follow_set(symbol):
    if symbol in follow:
        return follow[symbol]

    follow[symbol] = set()
    
    if symbol == initial_variable:
        follow[symbol].add('$')

    head_prods = find_head_productions(symbol)

    for A in head_prods:
        for prod in head_prods[A]:
            index = prod.index(symbol)

            if index + 1 < len(prod):
                b = prod[index + 1]

                if is_terminal(b):
                    follow[symbol].add(b)

                elif b in first:
                    follow[symbol].update(first[b] - {''})

                    if '' in first[b]:
                        follow[symbol].update(make_follow_set(A))
            else:
                follow[symbol].update(make_follow_set(A))

    return follow[symbol]