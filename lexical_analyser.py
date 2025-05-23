VARIABLES = ['E', 'E-', 'T', 'T-', 'F']
TOKENS = ['id', '+', '*', '(', ')']

initial_variable = 'E'

G = {
    'E': [['T', 'E-']],
    'E-': [['+', 'T', 'E-'], ['']],
    'T': [['F', 'T-']],
    'T-': [['*', 'F', 'T-'], ['']],
    'F': [['id'], ['(', 'E', ')']]
}

M_table = {}
first = {}
follow = {}

def is_terminal(symbol):
    return symbol in TOKENS


def make_first_set(symbol):
    if (symbol in first):
        return first[symbol]

    if (is_terminal(symbol) or symbol == ''):
        return {symbol}
    
    first[symbol] = set()

    for prod in G[symbol]:
        if len(prod) > 0:
            first[symbol] |= make_first_set(prod[0])

    return first[symbol]

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
                    follow[symbol].update(first[b])

                    if '' in first[b]:
                        follow[symbol].update(make_follow_set(A))
            else:
                follow[symbol].update(make_follow_set(A))

    return follow[symbol]
   
def make_Mtable():
    for var in G:
        make_first_set(var)

    for var in G:
        make_follow_set(var)

    for var in follow:
        print(var, follow[var])

    print("\n")

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

make_Mtable()

def predetive_descending_analysis(expression):
    expression = expression + ['$']
    stack = [initial_variable]

    i = 0
    char = expression[0]

    while(stack and i < len(expression)):
        top = stack[-1]

        if (is_terminal(top)):
            if (top == char):
                stack.pop()
                i = i + 1
                char = expression[i]
            else:
                return False
        else:
            if top not in M_table or char not in M_table[top]:
                return False

            derivation = M_table[top][char]
            stack.pop()

            if derivation != ['']:  
                for symbol in reversed(derivation):
                    stack.append(symbol)

    return len(stack) == 0 and char == '$'