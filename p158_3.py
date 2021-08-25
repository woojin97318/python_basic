numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# 짝수 홀수 구분 01
print("# 짝수 홀수 구분 01")
for number in numbers:
    if number % 2 == 0:
        print("{} 는 짝수입니다.".format(number))
    else:
        print("{} 는 홀수입니다.".format(number))
print()

# 짝수 홀수 구분 02
print("# 짝수 홀수 구분 02")
holzzak = ["짝수", "홀수"]
for number in numbers:
    print("{} 는 {}입니다.".format(number, holzzak[number % 2]))
print()

# 자릿수 구분 코드
print("# 자릿수 구분")
for number in numbers:
    print("{} 는 {} 자릿수입니다.".format(number, len(str(number))))