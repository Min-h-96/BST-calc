import sys


def postfix(list):
    # 숫자와 연산자를 각각 구분을 한다
    for i in range(len(list)):
        operands = []
        operator = []
        for i in list:
            if ord(i) >= 48:
                operands.append(i)
            else:
                operator.append(i)

        lst_postfix = [operands[0]]
        for i in range(len(operator)):
            lst_postfix.append(operands[i+1])
            lst_postfix.append(operator[i])

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
        if ord(data) >= 49:
            # 이미 오른쪽 자식 노드에 수가 있을 경우
            if currentNode.right:
                if currentNode.left:  # 왼쪽 자식 노드에 연산자 있는 경우
                    self.insertNode(currentNode.left, data)
                else:  # 없는 경우
                    currentNode.left = Node(data)
            # 없을 경우
            else:
                currentNode.right = Node(data)
        # operator가 들어왔을 때
        else:
            if currentNode.left:
                self.insertNode(currentNode.left, data)
            else:
                currentNode.left = Node(data)

    def calculate(self):
        return self.calculateNode(self.root)

    def calculateNode(self, currentNode):
        # 루트 노드 값이 operand가 되면 그 값을 return
        if ord(self.root.data[0]) >= 48:
            return self.root.data
        # 왼쪽 자식 노드 값이 operand 이면 부모 노드의 operator로 계산
        if ord(currentNode.left.data[0]) >= 49:
            if currentNode.data == '+':
                currentNode.data = str(
                    float(currentNode.left.data) + float(currentNode.right.data))
            elif currentNode.data == '-':
                currentNode.data = str(
                    float(currentNode.left.data) - float(currentNode.right.data))
            elif currentNode.data == '*':
                currentNode.data = str(
                    float(currentNode.left.data) * float(currentNode.right.data))
            elif currentNode.data == '/':
                currentNode.data = str(round(float(currentNode.left.data) / float(currentNode.right.data), 1))
            return self.calculateNode(self.root)
        # 왼쪽 자식 노드 값이 operator이면 그 노드로 이동해서 함수 재귀 호출
        else:
            return self.calculateNode(currentNode.left)


if __name__ == "__main__":
    prob = list(map(str, sys.stdin.readline().split()))
    # arr = ['2', '+', '7', '*', '5', '-', '7']
    postfix_form = postfix(prob)

    bst = BinarySearchTree()
    for i in reversed(postfix_form):
        bst.insert(i)
    print(postfix_form)
    print(bst.calculate())
