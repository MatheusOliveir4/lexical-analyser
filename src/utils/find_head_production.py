from grammar import G

def find_head_productions(symbol):
    head_prods = {}

    for var in G:
        if (var != symbol):
            for prod in G[var]:
                if (symbol in prod):
                    if var not in head_prods:
                        head_prods[var] = []
                    head_prods[var].append(prod)

    return head_prods