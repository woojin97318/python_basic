# 숫자는 무작위로 입력해도 상관없습니다.
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

# 작성합니다.
for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]

# 최종 출력
print(character)