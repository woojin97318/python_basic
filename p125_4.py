a = float(input("1번쨰 숫자 입력> "))
b = float(input("2번째 숫자 입력> "))
print()

if a > b:
    print("처음 입력했던 {}가 {}보다 큽니다.".format(a, b))

if a < b:
    print("두 번째로 입력했던 {}가 {}보다 큽니다.".format(b, a))