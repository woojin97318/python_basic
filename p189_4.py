max_value = 0
a = 0
b = 0

for i in range(0, 100, 1):
    j = 100 - i
    # 최대값 구하기
    if max_value < i * j:
        max_value = i * j
        a = i
        b = j

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))