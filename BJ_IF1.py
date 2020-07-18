#BJ_IF1
#두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

A, B = map(int,input().split())
# map(func,x) 맵함수는 객체 각각에 func함수를 적용

if A>B:
    print('>')
elif A<B:
    print('<')
else:
    print('==')
