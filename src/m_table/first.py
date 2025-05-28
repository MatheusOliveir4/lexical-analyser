from grammar import G
from utils.is_terminal import is_terminal

first = {}

def make_first_set(symbol):
    if symbol in first:
        return first[symbol]

    if is_terminal(symbol) or symbol == '' or symbol not in G:
        return {symbol}
    
    first[symbol] = set()

    for prod in G[symbol]:
        if len(prod) == 0:
            first[symbol].add('')
            
        elif is_terminal(prod[0]) or prod[0] == '':
            first[symbol].add(prod[0])
            
        else:
            first[symbol].update(make_first_set(prod[0]))

    return first[symbol]