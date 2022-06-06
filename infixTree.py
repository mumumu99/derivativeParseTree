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