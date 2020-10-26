import sys


def postfix(list):
    for i in range(len(list)-1):
        if 46 < ord(list[i]) < 58 or ord(list[i]) == 42 or ord(list[i]) == 43 or ord(list[i]) == 45:
            if (ord(list[i]) > 47 and ord(list[i+1]) > 47) or (ord(list[i]) <= 47 and ord(list[i+1]) <= 47):
                print('입력한 식이 올바르지 않습니다.')
                exit(0)
            else:
                pass
        else:
            print('입력한 식이 올바르지 않습니다.')
            exit(0)
    # 숫자와 연산자를 각각 구분을 한다
    for i in range(len(list)):
        operands = []
        operator = []
        lst_postfix = []
        for i in range(len(list)):
            # 숫자인 경우
            if ord(list[i]) >= 48:
                operands.append(list[i])
            # 연산자인 경우
            else:
                if operator and (list[i] == '+' or list[i] == '-'):
                    if len(operands) > len(operator):
                        count = 2
                        while count > 0:
                            lst_postfix.append(operands[0])
                            del operands[0]
                            count -= 1
                        while operands:
                            lst_postfix.append(operands[0])
                            del operands[0]
                            lst_postfix.append(operator[0])
                            del operator[0]
                        while operator:
                            lst_postfix.append(operator[0])
                            del operator[0]
                    else:
                        lst_postfix.append(operands[0])
                        del operands[0]
                        while operands:
                            lst_postfix.append(operands[0])
                            del operands[0]
                            lst_postfix.append(operator[0])
                            del operator[0]
                        while operator:
                            lst_postfix.append(operator[0])
                            del operator[0]
                
                operator.append(list[i])
                if list[i] == '*' or list[i] == '/':
                    if operator[len(operator)-2] == '+' or operator[len(operator)-2] == '-':
                        operator[len(operator)-1], operator[len(operator)-2] = operator[len(operator)-2], operator[len(operator)-1]

    if len(operands) > len(operator):
        count = 2
        while count > 0:
            lst_postfix.append(operands[0])
            del operands[0]
            count -= 1
        while operands:
            lst_postfix.append(operands[0])
            del operands[0]
            lst_postfix.append(operator[0])
            del operator[0]
        while operator:
            lst_postfix.append(operator[0])
            del operator[0]
    else:
        lst_postfix.append(operands[0])
        del operands[0]
        while operands:
            lst_postfix.append(operands[0])
            del operands[0]
            lst_postfix.append(operator[0])
            del operator[0]
        while operator:
            lst_postfix.append(operator[0])
            del operator[0]

    return lst_postfix


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        # 루트 노드가 존재하지 않으면 루트 노드 생성
        if self.root is None:
            self.root = Node(data)
        else:
            self.insertNode(self.root, data)
    
    def insertNode(self, currentNode, data):
        # operand가 들어왔을 때
        if ord(data) >= 48:
            # 이미 오른쪽 자식 노드에 수가 있을 경우
            if currentNode.left:
                currentNode.right = Node(data)
            # 없을 경우
            else:
                currentNode.left = Node(data)
        # operator가 들어왔을 때
        else:
            self.calculateNode(self.root, data)

    def calculateNode(self, current, data):
        if current.right:
            if data == '+':
                current.left.data = str(float(current.left.data) + float(current.right.data))
                current.right = None
            elif data == '-':
                current.left.data = str(float(current.left.data) - float(current.right.data))
                current.right = None
            elif data == '*':
                current.left.data = str(float(current.left.data) * float(current.right.data))
                current.right = None
            elif data == '/':
                try:
                    current.left.data = str(round(float(current.left.data) / float(current.right.data), 1))
                    current.right = None
                except ZeroDivisionError:
                    print('0으로 나누는 경우가 존재합니다.')
                    exit(0)
        else:
            if data == '+':
                current.data = str(float(current.data) + float(current.left.data))
                current.left = None
            elif data == '-':
                current.data = str(float(current.data) - float(current.left.data))
                current.left = None
            elif data == '*':
                current.data = str(float(current.data) * float(current.left.data))
                current.left = None
            elif data == '/':
                try:
                    current.data = str(round(float(current.data) / float(current.left.data), 1))
                    current.left = None
                except ZeroDivisionError:
                    print('0으로 나누는 경우가 존재합니다.')
                    exit(0)

    def print(self):
        return self.root.data


if __name__ == "__main__":
    prob = list(map(str, sys.stdin.readline().split()))

    postfix_form = postfix(prob)
    print(postfix_form)

    bst = BinarySearchTree()
    for i in postfix_form:
        bst.insert(i)
    
    print(bst.print())

    # prob1 = ['2', '+', '7', '*', '5', '-', '6'] # 2 7 5 * + 6 -
    # prob2 = ['5', '+', '4', '-', '2', '*', '3', '+', '6'] # 5 4 + 2 3 * - 6 +
    # prob3 = ['1', '-', '2', '*', '3', '/', '4', '+', '5'] # 1 2 3 * 4 / - 5 +
    # prob4 = ['1', '*', '2', '+', '3', '*', '2', '/', '4', '+', '5'] # 1 2 * 3 2 * 4 / + 5 +
    # print(postfix(prob1))
    # print(postfix(prob2))
    # print(postfix(prob3))
    # print(postfix(prob4))