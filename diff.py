##################################################################################################
# diff(expression, var) Devuelve la derivada de expression respecto a la variable var
# expression es una expresion en notacion SQRPN
# var es una variable de derivacion, por ejemplo, "x"
##################################################################################################
def diff(expression, var):
    if expression[0] =='+':
        derivative = ['+',diff(expression[1],var),diff(expression[2],var)]

    elif expression[0]== '*':
        derivative =['+',['*', diff(expression[1],var), expression[2]],['*', expression[1], diff(expression[2],var)]]

    elif expression[0] == var:
        derivative = '1'

    elif expression[0] == "sin":
        derivative = ['*', ["cos", expression[1]], diff(expression[1],var)]

    else:
        derivative = '0'

    return derivative
