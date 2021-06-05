from simplify import simplify
from SQRPN import SQRPN
from infix import infix
from diff2 import diff
from SYA import SYA
from tokenizer import tokenize


#var = 'x'
#exp = "a*x^4"

#print("Funcion: ", exp)

#exp = tokenize(exp)

#print("Tokenized: ", exp)
#exp = SYA(exp)

#exp = SQRPN(exp)


#deriv = diff(exp,var)
#counts = 0

#while counts < 50 and deriv != simplify(deriv):
#    deriv = simplify(deriv)
#    counts = counts + 1

#print("counts: ", counts)

#print ("Derivada: ", infix(deriv))

#print("\n")


##################### Input #####################
exp = ''
var = ''

while exp != "exit" and var != "exit":
    print("\n \n -------------------------------------------------------------------------------------------\n")
    print("SYMBDIFF v1 (programado por Miguel Armayor Martinez)\n")
    print("Para salir del programa introducir 'exit' (sin comillas).\n")
    print("La funcion introducida debe estar escrita con todos los parentesis necesarios. Ejemplo: ")
    print("-cos(x^2+a)*(7/2)+x^(cos(x))\n")
    print("Debe especificarse la variable respecto de la cual se quiere la derivada.\n\n")
    exp = input('Expresion: ')
    if exp == "exit":
        break
    var = input('Variable de derivacion: ')
    if var == "exit":
        break
    print("\n\n")

    exp = tokenize(exp)
    exp = SYA(exp)
    exp = SQRPN(exp)
    deriv = diff(exp,var)
    counts = 0

    while counts < 50 and deriv != simplify(deriv):
        deriv = simplify(deriv)
        counts = counts + 1





    ##################### OUTPUT #####################

    
    print ("Derivada: ", infix(deriv))

    print("\n")

    print("\n \n -------------------------------------------------------------------------------------------\n")
