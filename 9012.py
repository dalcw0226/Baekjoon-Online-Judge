# 9012 - 괄호

N = int(input())
for i in range(N):
    sample = input()
    while sample.find("()") != -1:
        sample = sample.replace("()", "")
    if len(sample) == 0:
        print("YES")
    else:
        print("NO")