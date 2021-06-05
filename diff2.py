##################################################################################################
# diff(expression, var) Devuelve la derivada de expression respecto a la variable var
# expression es una expresion en notacion SQRPN
# var es una variable de derivacion, por ejemplo, "x"
##################################################################################################
def diff(expression, var):

    # Derivada de una suma o una resta
    if expression[0] =='+' or expression[0] =='-':
        return [expression[0],diff(expression[1],var),diff(expression[2],var)]
    
    # Derivada del producto
    elif expression[0]== '*':
        return ['+',['*', diff(expression[1],var), expression[2]],['*', expression[1], diff(expression[2],var)]]

    # Derivada de un cociente
    elif expression[0]== '/':
        return ['/',["-",['*', diff(expression[1],var), expression[2]], ['*', expression[1], diff(expression[2],var)]],['^', expression[2], "2"]]

    elif expression[0] == "sin":
        return ['*', ["cos", expression[1]], diff(expression[1],var)]

    elif expression[0] == "cos":
        return ['-',"0", ['*', ["sin", expression[1]], diff(expression[1],var)]]
    
    elif expression[0] == "exp":
        return ['*',["exp",expression[1]], diff(expression[1],var)]

    elif expression[0] == "log":
        return ["/",diff(expression[1],var), expression[1]]
    
    elif expression[0] == "^":
        return ["+", ["*", ["^", expression[1],expression[2]] , ["*", diff(expression[2], var), ["log", expression[1]]] ], ["*",expression[2] ,["*", diff(expression[1], var), ["^", expression[1], ["-", expression[2],'1']]]] ]
    elif expression[0] == var:
        return '1'

    else:
        return '0'

    #return expression
