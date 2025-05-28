from grammar import G, VARIABLES, TOKENS
from m_table.first import first, make_first_set
from m_table.follow import follow, make_follow_set
from utils.is_terminal import is_terminal

M_table = {}

def make_Mtable():
    for var in G:
        make_first_set(var)

    for var in G:
        make_follow_set(var)

    for var in VARIABLES:
        M_table[var] = {}
        for token in TOKENS:
            M_table[var][token] = {}

        M_table[var]['$'] = {}

    for A in G:
        M_table[A] = {}

        for prod in G[A]:
            if (prod[0] in first) :
                for terminal in first[prod[0]]:
                    M_table[A][terminal] = {}
                    M_table[A][terminal] = prod

            elif(is_terminal(prod[0])):
                M_table[A][prod[0]] = {}
                M_table[A][prod[0]] = prod
            
            if (prod[0] == ''):
                for terminal in follow[A]:
                    M_table[A][terminal] = {}
                    M_table[A][terminal] = prod
