# 2609 최대공약수와 최소공배수
# 배운 알고리즘을 구현해보자

x, y = map(int, input().split())

# GCD 알고리즘을 이용하자 -> 최대공약수 구하기
x_, y_ = x, y
while True:
    if x_ < y_:
        x_, y_ = y_, x_
    x_ = x_ % y_
    if x_ == 0:
        break
MAX = y_

# 최소공배수 구하는 알고리즘..?
a = x / MAX
b = y / MAX
MIN = a * b * MAX

print(MAX)
print(int(MIN))