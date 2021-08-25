# 1 ~ 100 / 2진수 / 0이 하나만 포함된 2진수 / 그들의 합
print("# 리스트 내포 사용x")
output = 0
for i in range(1, 101, 1):
    if "{:b}".format(i).count("0") == 1:
        print("{} : {:b}".format(i, i))
        output += i
print("합계 : {}".format(output))
print()

# 리스트 내포 사용
print("# 리스트 내포 사용")
output1 = [i for i in range(1, 101, 1) if "{:b}".format(i).count("0") == 1]
print("합계 : {}".format(sum(output1)))