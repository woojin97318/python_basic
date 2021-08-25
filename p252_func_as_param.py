# 매개변수로 받은 함수를 10번 호출하는 함수
def call_10_times(func):
    for i in range(10):
        func(i)

# 간단한 출력하는 함수
def print_hello(number):
    print("안녕하세요", number)

# 조합하기
call_10_times(print_hello)

# 람다를 이용
print("# 람다")
call_10_times(lambda number: print("안녕하세요", number))