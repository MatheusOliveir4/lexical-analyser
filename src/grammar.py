TOKENS = [
    'x',
    "NUM_INT",
    "NUM_DEC",
    "ID",
    "TEXTO",
    "int",
    "float",
    "double",
    "char",
    "boolean",
    "void",
    "if",
    "else",
    "for",
    "while",
    "switch",
    "case",
    "default",
    "break",
    "continue",
    "return",
    "struct",
    "main",
    "scanf",
    "println",
    "COMMENT_SINGLE_LINE",
    "COMMENT_MULTI_LINE",
    "=",
    "+",
    "-",
    "*",
    "/",
    "%",
    "&&",
    "||",
    "!",
    ">",
    ">=",
    "<",
    "<=",
    "!=",
    "==",
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    ",",
    ";",
    "+=",
    "-=",
    "*=",
    "/=",
    "%=",
    "&&=",
    "||=",
    "->",
    "..."
]

initial_variable = 'Programa'

G = {

    'Programa': [
        ['ListaDeclaracao_Opt']
    ],

    'ListaDeclaracao_Opt': [
        ['Declaracao', 'ListaDeclaracao_Opt'],
        ['']
    ],

    'Declaracao': [
        ['Tipo', 'ID', 'Declaracao_Sux_Aer_ID'],
        ['struct', 'ID', '{', 'ListaDeclaracaoVariavel_Opt', '}', ';'],
        ['Comentario']
    ],

    'Declaracao_Sux_Aer_ID': [
        ['DeclaracaoVariavel_Rest'],
        ['(', 'Parametros_Opt', ')', 'Bloco']
    ],

    'ListaDeclaracaoVariavel_Opt': [
        ['DeclaracaoVariavel', 'ListaDeclaracaoVariavel_Opt'],
        ['']
    ],

    'DeclaracaoVariavel': [
        ['Tipo', 'ID', 'DeclaracaoVariavel_Rest']
    ],

    'DeclaracaoVariavel_Rest': [
        [';'],
        ['=', 'Expressao', ';']
    ],

    'Tipo': [
        ['int'], ['float'], ['double'], ['char'], ['boolean']
    ],

    'DeclaracaoFuncao_Body': [
        ['(', 'Parametros_Opt', ')', 'Bloco']
    ],

    'Parametros_Opt': [
        ['Parametros'],
        ['']
    ],
  
    'Parametros': [
        ['Parametro', 'Parametros_Tail_Opt']
    ],
  
    'Parametros_Tail_Opt': [
        [',', 'Parametros'],
        ['']
    ],
  
    'Parametro': [
        ['Tipo', 'Parametro_Kind']
    ],
  
    'Parametro_Kind': [
        ['ID', 'Parametro_Array_Spec_Opt'],
        ['...', 'ID']
    ],
  
    'Parametro_Array_Spec_Opt': [
        ['[', ']'],
        ['']
    ],

    'Bloco': [
        ['{', 'ListaDeclaracao_Opt', '}']
    ],

    'Comentario': [
        ['COMMENT_SINGLE_LINE'],
        ['COMMENT_MULTI_LINE']
    ],

    'Atribuicao_RHS': [
        ['AssignOpExpr', 'Expressao']
    ],

    'AssignOpExpr': [
        ['='], ['+='], ['-='], ['*='], ['/='], ['%='], ['&&='], ['||=']
    ],

    'EstruturaControle': [
        ['if', '(', 'Expressao', ')', 'Bloco', 'EstruturaControle_Else_Opt'],
        ['while', '(', 'Expressao', ')', 'Bloco'],
        ['for', '(', 'Expressao_Opt', ';', 'Expressao_Opt', ';', 'Expressao_Opt', ')', 'Bloco'],
        ['switch', '(', 'Expressao', ')', 'CaseLista'],
        ['break', ';'],
        ['continue', ';'],
        ['return', 'Expressao_Opt_Return']
    ],
  
    'EstruturaControle_Else_Opt': [
        ['else', 'Bloco'],
        ['']
    ],
  
    'Expressao_Opt': [
        ['Expressao'],
        ['']
    ],
  
    'Expressao_Opt_Return': [
        ['Expressao', ';'],
        [';']
    ],
  
    'CaseLista': [
        ['ListaCaseDecl_Opt']
    ],
  
    'ListaCaseDecl_Opt': [
        ['CaseDecl', 'ListaCaseDecl_Opt'],
        ['']
    ],
  
    'CaseDecl': [
        ['case', 'Expressao', ':', 'Bloco'],
        ['default', ':', 'Bloco']
    ],

    'Array_Access_Sux': [
        ['[', 'Expressao', ']']
    ],
  
    'Array_Declaration_Modier_Opt': [
        ['[', ']'],
        ['']
    ],
  
    'ArrayInicializacao': [
        ['{', 'ExpressaoLista_Opt', '}']
    ],
  
    'ExpressaoLista_Opt': [
        ['ExpressaoLista'],
        ['']
    ],
  
    'ExpressaoLista': [
        ['Expressao', 'ExpressaoLista_Tail_Opt']
    ],
  
    'ExpressaoLista_Tail_Opt': [
        [',', 'ExpressaoLista'],
        ['']
    ],

    'Expressao': [
        ['Primaria_Start_Expr', 'Expressao_Chain'],
        ['Unary_Prex_Op', 'ExpressaoUnaria_Operand', 'Expressao_Chain_From_UnOp'],
        ['(', 'Expressao', ')', 'Expressao_Chain_From_Paren'],
        ['ID', 'Expressao_Aer_ID_Choice']
    ],
  
    'Expressao_Aer_ID_Choice': [
        ['AssignOpExpr', 'Expressao'],
        ['ExpressaoPosix_Sux_Chain_Opt', 'Expressao_Chain']
    ],
  
    'Primaria_Start_Expr': [
        ['NUM_INT'], ['NUM_DEC'], ['TEXTO']
    ],
  
    'Expressao_Chain': [
        ['ExpressaoLogicaOR_Prime']
    ],
  
    'Expressao_Chain_From_UnOp': [
        ['ExpressaoMultiplicativa_Prime', 'ExpressaoAditiva_Prime', 'ExpressaoRelacional_Equality_Prime', 'ExpressaoLogicaAND_Prime', 'ExpressaoLogicaOR_Prime']
    ],
  
    'Expressao_Chain_From_Paren': [
        ['ExpressaoPosix_Sux_Chain_Opt', 'ExpressaoLogicaOR_Prime']
    ],
  
    'ExpressaoLogicaOR_Prime': [
        ['||', 'ExpressaoLogicaAND', 'ExpressaoLogicaOR_Prime'],
        ['']
    ],
  
    'ExpressaoLogicaAND': [
        ['ExpressaoRelacional_Equality', 'ExpressaoLogicaAND_Prime']
    ],
  
    'ExpressaoLogicaAND_Prime': [
        ['&&', 'ExpressaoRelacional_Equality', 'ExpressaoLogicaAND_Prime'],
        ['']
    ],
  
    'ExpressaoRelacional_Equality': [
        ['ExpressaoAditiva', 'ExpressaoRelacional_Equality_Prime']
    ],
  
    'ExpressaoRelacional_Equality_Prime': [
        ['RelationalOp', 'ExpressaoAditiva', 'ExpressaoRelacional_Equality_Prime'],
        ['']
    ],
  
    'RelationalOp': [
        ['>'], ['>='], ['<'], ['<='], ['!='], ['==']
    ],
  
    'ExpressaoAditiva': [
        ['ExpressaoMultiplicativa', 'ExpressaoAditiva_Prime']
    ],
  
    'ExpressaoAditiva_Prime': [
        ['+', 'ExpressaoMultiplicativa', 'ExpressaoAditiva_Prime'],
        ['-', 'ExpressaoMultiplicativa', 'ExpressaoAditiva_Prime'],
        ['']
    ],
  
    'ExpressaoMultiplicativa': [
        ['ExpressaoUnaria', 'ExpressaoMultiplicativa_Prime']
    ],
  
    'ExpressaoMultiplicativa_Prime': [
        ['*', 'ExpressaoUnaria', 'ExpressaoMultiplicativa_Prime'],
        ['/', 'ExpressaoUnaria', 'ExpressaoMultiplicativa_Prime'],
        ['%', 'ExpressaoUnaria', 'ExpressaoMultiplicativa_Prime'],
        ['']
    ],
  
    'ExpressaoUnaria': [
        ['ExpressaoPosix'],
        ['Unary_Prex_Op', 'ExpressaoUnaria_Operand']
    ],
  
    'Unary_Prex_Op': [
        ['-'], ['++'], ['--']
    ],
  
    'ExpressaoUnaria_Operand': [
        ['ExpressaoUnaria'],
        ['ExpressaoPosix']
    ],
  
    'ExpressaoPosix': [
        ['Primaria', 'ExpressaoPosix_Sux_Chain_Opt']
    ],
  
    'ExpressaoPosix_Sux_Chain_Opt': [
        ['ExpressaoPosix_Sux', 'ExpressaoPosix_Sux_Chain_Opt'],
        ['']
    ],
  
    'ExpressaoPosix_Sux': [
        ['[', 'Expressao', ']'],
        ['(', 'Argumentos_Opt', ')'],
        ['.', 'ID'],
        ['->', 'ID']
    ],
  
    'Primaria': [
        ['ID'],
        ['NUM_INT'],
        ['NUM_DEC'],
        ['TEXTO'],
        ['(', 'Expressao', ')'],
        ['ArrayInicializacao']
    ],
  
    'Argumentos_Opt': [
        ['Argumentos'],
        ['']
    ],
  
    'Argumentos': [
        ['ExpressaoLista']
    ]
}

VARIABLES = list(G.keys())
