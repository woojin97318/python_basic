# 변수를 선언합니다.
list_number = [52, 273, 32, 72, 100]

# try except 구문으로 예외를 처리합니다.
try:
    # 숫자를 입력받습니다.
    number_input_a = int(input("정수 입력> "))
    # 리스트의 첫번째 요소를 출력합니다.
    print("{}번째 요소: {}".format(number_input_a, list_number[number_input_a]))
except ValueError as exception:
    print("정수를 입력해주세요!")
    print("exception:", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print("exception:", exception)