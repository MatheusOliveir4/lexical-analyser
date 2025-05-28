from parser import predictive_descending_analysis

expr1 = ['int', 'ID', ';']
resultado = predictive_descending_analysis(expr1) 

print(f"Resultado para expr1: {resultado}")  

expr2 = ['struct', 'ID', '{', 'int', 'ID', ';', '}', ';']
resultado = predictive_descending_analysis(expr2) 

print(f"Resultado para expr2: {resultado}")  

expr_fail1 = ['int', 'ID']
resultado = predictive_descending_analysis(expr_fail1) 

print(f"Resultado para expr_fail1: {resultado}")  

expr_fail2 = ['void', 'ID', 'int', 'ID', '{', '}']
resultado = predictive_descending_analysis(expr_fail2) 

print(f"Resultado para expr_fail2: {resultado}")  