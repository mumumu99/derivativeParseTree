import argparse

parser = argparse.ArgumentParser(description='Derivative of symbolic expression.')
parser.add_argument('--exp', required=True, help='expression')
parser.add_argument('--var', required=True, help='variable')
args = parser.parse_args()

# print(args.exp)
# print(args.var)

from tokenizer import tokenize
from postfix_SYA import postfix
from buildParseTree import buildParseTree
from diffTree import diffTree
from simplifyTree import simplifyTree
from infixTree import infixTree

def is_function(car):
    function_list = ["cos", "sin", "tan", "exp", "log"]
    if car in function_list:
        return 1
    else:
        return 0

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

exp = args.exp
var = args.var
# exp = "x^(-4)-x^3-x^2-x-1+sin(x)"
# exp = "sin(x^2+x)+x"
# exp = 'sin(x)'
# exp = 'x*y*x*y*x'
# exp = '-12*(-a-cos(x)*3)-2'
print("Funcion: ", exp)

exp = tokenize(exp)
print("Tokenized: ", exp)

exp = postfix(exp)
print("postfix: ", exp)

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