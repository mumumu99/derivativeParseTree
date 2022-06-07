from pythonds.basic import Stack
from pythonds.trees import BinaryTree
from pythonds.trees import *

def buildParseTree(fpexp):
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    
    for c in fpexp:

        if is_operator(c):
            tempTree = BinaryTree(c)
            tempTree.rightChild = pStack.pop()
            tempTree.leftChild = pStack.pop()

            pStack.push(tempTree)
            
        elif is_function(c):
            tempTree = BinaryTree(c)
            # tempTree.leftChild = pStack.pop()
            tempTree.rightChild = pStack.pop()

            pStack.push(tempTree)
        
        else:
            pStack.push(BinaryTree(c))
        
    return tempTree

##################################################################################################
# Funciones Auxiliares
##################################################################################################
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