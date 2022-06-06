##################################################################################################
# diff(expression, var) Devuelve la derivada de expression respecto a la variable var
# expression es una expresion en notacion SQRPN
# var es una variable de derivacion, por ejemplo, "x"
##################################################################################################
from pythonds.trees import BinaryTree

def diffTree(parseTree, var):
    current = parseTree.getRootVal()
    F = parseTree.leftChild
    G = parseTree.rightChild
    # Derivada de una suma o una resta
    if current =='+' or current =='-':
        tempTree = BinaryTree(current)
        tempTree.leftChild = diffTree(F,var)
        tempTree.rightChild = diffTree(G,var)
        return tempTree
        
    # Derivada del producto
    elif current == '*':
        tempTree = BinaryTree('+')
        tempTree.insertLeft('*')
        tempTree.insertRight('*')
        tempTree.leftChild.leftChild = diffTree(F,var)
        tempTree.leftChild.rightChild = G
        tempTree.rightChild.leftChild = F
        tempTree.rightChild.rightChild = diffTree(G,var)
        return tempTree
        
    # Derivada de un cociente
    elif current == '/':
        tempTree1 = BinaryTree('-')
        tempTree1.insertLeft('*')
        tempTree1.insertRight('*')
        tempTree1.leftChild.leftChild = diffTree(F,var)
        tempTree1.leftChild.rightChild = G
        tempTree1.rightChild.leftChild = F
        tempTree1.rightChild.rightChild = diffTree(G,var)

        tempTree2 = BinaryTree('^')
        tempTree2.leftChild = F
        tempTree2.insertRight('2')

        tempTree = BinaryTree('/')
        tempTree.leftChild = tempTree1
        tempTree.rightChild = tempTree2
        
        return tempTree

    elif current == "sin":
        tempTree = BinaryTree('*')
        tempTree.insertLeft('cos')
        # tempTree.leftChild.leftChild = F
        # tempTree.rightChild = diffTree(F,var)
        tempTree.leftChild.rightChild = G
        tempTree.rightChild = diffTree(G,var)
        return tempTree

    elif current == "cos":
        tempTree = BinaryTree('-')
        tempTree.insertLeft('0')
        tempTree.insertRight('*')
        tempTree.rightChild.insertLeft('sin')
        # tempTree.rightChild.leftChild.leftChild = F
        # tempTree.rightChild.rightChild = diffTree(F,var)
        tempTree.rightChild.leftChild.rightChild = G
        tempTree.rightChild.rightChild = diffTree(G,var)
        return tempTree

    elif current == "exp":
        tempTree = BinaryTree('*')
        tempTree.insertLeft('exp')
        # tempTree.leftChild.leftChild = F
        # tempTree.rightChild = diffTree(F,var)
        tempTree.leftChild.rightChild = G
        tempTree.rightChild = diffTree(G,var)
        return tempTree

    elif current == "log":
        tempTree = BinaryTree('/')
        # tempTree.leftChild = diffTree(F,var)
        # tempTree.rightChild = F
        tempTree.leftChild = diffTree(G,var)
        tempTree.rightChild = G

        return tempTree
    
    elif current == "^":
        tempTree1 = BinaryTree('*')
        tempTree1.insertLeft('^')
        tempTree1.insertRight('*')
        tempTree1.leftChild.leftChild = F
        tempTree1.leftChild.rightChild = G
        tempTree1.rightChild.leftChild = diffTree(G,var)
        tempTree1.rightChild.insertRight('log')
        # tempTree1.rightChild.rightChild.leftChild = F
        tempTree1.rightChild.rightChild.rightChild = F

        tempTree2 = BinaryTree('*')
        tempTree2.leftChild = G
        tempTree2.insertRight('*')
        tempTree2.rightChild.leftChild = diffTree(F,var)
        tempTree2.rightChild.insertRight('^')
        tempTree2.rightChild.rightChild.leftChild = F
        tempTree2.rightChild.rightChild.insertRight('-')
        tempTree2.rightChild.rightChild.rightChild.leftChild = G
        tempTree2.rightChild.rightChild.rightChild.insertRight('1')

        tempTree = BinaryTree('+')
        tempTree.leftChild = tempTree1
        tempTree.rightChild = tempTree2

        return tempTree
    
    elif current == var:
        return BinaryTree('1')

    else:
        return BinaryTree('0')


# pt1 = BinaryTree('sin')
# pt1.insertLeft('x')
# pt2 = BinaryTree('x')
# pt = BinaryTree('+')
# pt.leftChild = pt1
# pt.rightChild = pt2
# diffTree(pt, 'x').printexp()
