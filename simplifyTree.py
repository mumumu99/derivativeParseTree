from pythonds.trees import BinaryTree

def simplifyTree(parseTree):
    
    if not isinstance(parseTree,BinaryTree):
        return parseTree
    
    else:
        current = parseTree.getRootVal()
        LTree = parseTree.leftChild
        RTree = parseTree.rightChild

        if is_function(current):
            tempTree = BinaryTree(current)
            tempTree.rightChild = simplifyTree(RTree)

            return tempTree
            #return  [expression[0], simplifyTree(expression[1])]

        else: 
            if current == '*':
                if LTree.getRootVal() == '1':
                    return simplifyTree(RTree)
                elif RTree.getRootVal() == '1':
                    return simplifyTree(LTree)
                elif LTree.getRootVal() == '0':
                    return BinaryTree('0')
                elif RTree.getRootVal() == '0':
                    return BinaryTree('0')
                elif is_operand(LTree.getRootVal()) and is_operand(RTree.getRootVal()) and RTree.getRootVal() == LTree.getRootVal():
                    tempTree = BinaryTree('^')
                    tempTree.leftChild = simplifyTree(LTree)
                    tempTree.insertRight('2')
                    return tempTree
                else:
                    tempTree = BinaryTree(current)
                    tempTree.leftChild = simplifyTree(LTree)
                    tempTree.rightChild = simplifyTree(RTree)
                    return tempTree
                    #return [expression[0],simplifyTree(expression[1]), simplifyTree(expression[2])]

            elif current == '+':
                if isinstance(LTree.getRootVal(), str) and isinstance(RTree.getRootVal(), str) and LTree.getRootVal().isnumeric() and RTree.getRootVal().isnumeric():
                    return BinaryTree(str(int(LTree.getRootVal())+int(RTree.getRootVal())))
                elif LTree.getRootVal() == '0':
                    return simplifyTree(RTree)
                elif RTree.getRootVal() == '0':
                    return simplifyTree(LTree)
                elif is_operand(LTree.getRootVal()) and is_operand(RTree.getRootVal()) and RTree.getRootVal() == LTree.getRootVal():
                    tempTree = BinaryTree('*')
                    tempTree.insertLeft('2')
                    tempTree.rightChild = simplifyTree(LTree)
                    return tempTree
                    #return ['*', '2', simplifyTree(expression[1])]
                else:
                    tempTree = BinaryTree(current)
                    tempTree.leftChild = simplifyTree(LTree)
                    tempTree.rightChild = simplifyTree(RTree)
                    return tempTree
                    #return [expression[0],simplifyTree(expression[1]), simplifyTree(expression[2])]

            elif current == '-':
                if isinstance(LTree.getRootVal(), str) and isinstance(RTree.getRootVal(), str) and LTree.getRootVal().isnumeric() and RTree.getRootVal().isnumeric() and int(LTree.getRootVal())>=int(RTree.getRootVal()):
                    return BinaryTree(str(int(LTree.getRootVal())-int(RTree.getRootVal())))
                if LTree.getRootVal() == '0' and RTree.getRootVal() == '0':
                    return BinaryTree('0')
                if RTree.getRootVal() == '0':
                    return simplifyTree(LTree)
                else:
                    tempTree = BinaryTree(current)
                    tempTree.leftChild = simplifyTree(LTree)
                    tempTree.rightChild = simplifyTree(RTree)
                    return tempTree
                    #return [expression[0],simplifyTree(expression[1]), simplifyTree(expression[2])]

            elif current == '^':
                if RTree.getRootVal() == '1':
                    return simplifyTree(LTree)
                elif RTree.getRootVal() == '0':
                    return BinaryTree('1')
                elif LTree.getRootVal() == '0':
                    return BinaryTree('0')
                else:
                    tempTree = BinaryTree(current)
                    tempTree.leftChild = simplifyTree(LTree)
                    tempTree.rightChild = simplifyTree(RTree)
                    return tempTree
                    #return [expression[0],simplifyTree(expression[1]), simplifyTree(expression[2])]
            
            # elif is_function(current):
            #     tempTree = BinaryTree(current)
            #     tempTree.leftChild = simplifyTree(LTree)
            #     return tempTree

            else:
                tempTree = BinaryTree(current)
                tempTree.leftChild = simplifyTree(LTree)
                tempTree.rightChild = simplifyTree(RTree)
                return tempTree
                #return [expression[0],simplifyTree(expression[1]), simplifyTree(expression[2])]


def is_operand(car):
    operand_list = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if car in operand_list:
        return 1
    else:
        return 0

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