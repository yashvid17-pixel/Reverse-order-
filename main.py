num = int(input())

if num < 0:
    num = -num

count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count = count + 1
        num = num // 10

print(count)