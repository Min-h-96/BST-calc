4학년 1학기 알고리즘 수업 내 프로젝트 #1 BST-calculator 입니다.

- 기능

1. Read a sequence of infix form
2. Parse it into a postfix expression
3. Build a binary tree representation of the expression
4. Print it in postfix form
5. Calculate and print its value
6. Any error messages for incorrect

- 주의점

1. stack 사용 Postfix Caculator가 아닌 BST 형태로 구현
2. 중간 과정 산출물들도 print되도록

- 난이도 1 : BST-calc-1.py

1. single-digit integers, binary operator : '+', '-', 'x', '/'
2. operand와 operator 사이에 space가 있다.
3. 연산자 우선 순위가 존재하지 않는다.
4. 소수 부분은 소수 둘 째 자리에서 반올림 한다.
5. Example : 2 + 4 x 5 / 4 = 7.5
