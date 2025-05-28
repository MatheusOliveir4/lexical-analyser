from grammar import initial_variable
from m_table.m_table import M_table, make_Mtable
from utils.is_terminal import is_terminal

def predictive_descending_analysis(expression):
    make_Mtable()
    
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