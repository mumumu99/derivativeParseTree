$ pip install pythonds

def infixTree(tree):
    if is_operator(tree.getRootVal()):
        if tree.getRootVal() == '-' and tree.leftChild.getRootVal() == '0':
            return  "(" +  tree.getRootVal() + infixTree(tree.rightChild) + ")"
        else:
            return  "(" + infixTree(tree.leftChild) + tree.getRootVal() + infixTree(tree.rightChild) + ")"
    elif is_function(tree.getRootVal()):
        return   tree.getRootVal() + "(" + infixTree(tree.rightChild) + ")"
    else:
        return tree.getRootVal()

def is_operator(car):
    operator_list = ["+", "-", "*", "/", "^"]
    if car in operator_list:
        return 1
    else:
        return 0
    
def is_function(car):
    function_list = ["cos", "sin", "tan", "exp", "log"]
    if car in function_list:
        return 1
    else:
        return 0


from simplify import simplify
from SQRPN import SQRPN
from infix import infix
from diff2 import diff
from SYA import SYA
from tokenizer import tokenize
from buildParseTree import buildParseTree
from diffTree import diffTree
from simplifyTree import simplifyTree

def is_function(car):
    function_list = ["cos", "sin", "tan", "exp", "log"]
    if car in function_list:
        return 1
    else:
        return 0

# def printexp(tree):
#     # function_brac = 0
#     # if tree.leftChild:
#     #     print('(', end=' ')
#     #     printexp(tree.getLeftChild())
#     # elif is_function(tree.getRootVal()):
#     #     function_brac += 1
#     # print(tree.getRootVal(), end=' ')
#     # if tree.rightChild:
#     #     printexp(tree.getRightChild())
#     #     if function_brac > 0:
#     #         function_brac -= 1
#     #     else:
#     #         print(')', end=' ')
#     if is_operator(tree.getRootVal()):
#         if tree.getRootVal() == '-' and tree.leftChild.getRootVal() == '0':
#             return  "(" +  tree.getRootVal() + printexp(tree.rightChild) + ")"
#         else:
#             return  "(" + printexp(tree.leftChild) + tree.getRootVal() + printexp(tree.rightChild) + ")"
#     elif is_function(tree.getRootVal()):
#         return   tree.getRootVal() + "(" + printexp(tree.rightChild) + ")"
#     else:
#         return tree

# identical
def identicalTrees(a, b):
     
    # 1. Both empty
    if a is None and b is None:
        return True
 
    # 2. Both non-empty -> Compare them
    if a is not None and b is not None:
        return ((a.getRootVal() == b.getRootVal()) and
                identicalTrees(a.leftChild, b.leftChild)and
                identicalTrees(a.rightChild, b.rightChild))
     
    # 3. one empty, one not -- false
    return False

var = 'x'
#exp = "x^(-4)-x^3-x^2-x-1+sin(x)"
exp = "sin(x^2+x)+x"
#exp = 'sin(x)'
#exp = 'x*y*x*y*x'
#exp = '-12*(-a-cos(x)*3)-2'
print("Funcion: ", exp)

exp = tokenize(exp)
print("Tokenized: ", exp)

exp = SYA(exp)
print("SYA: ", exp)

pt = buildParseTree(exp)
print("buildParseTree: ", infixTree(pt))

diff_pt = diffTree(pt,var)
print("differativeTree: ", infixTree(diff_pt))
print('\n')

simp_diff_pt = simplifyTree(diff_pt)

print('Simplifying...')
counts = 0
while counts < 50 and not identicalTrees(simp_diff_pt, simplifyTree(simp_diff_pt)):
   simp_diff_pt = simplifyTree(simp_diff_pt)
   print(infixTree(simp_diff_pt))
   print('\n')
   counts = counts + 1

print("counts: ", counts)