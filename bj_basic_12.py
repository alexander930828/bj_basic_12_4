#1

n = int(input())


numbers = []


for _ in range(n):
    numbers.append(int(input()))

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

for n in numbers:
    print(n)


#2

from sys import stdin

n = int(stdin.readline())

arr = []

for i in range(n):
    arr.append(int(stdin.readline())

arr.sort()

for i in arr:
    print(i)


#3

import sys

n = int(input())

check_list = [0] * 10001

for i in range(n):
    input_num = int(sys.stdin.readline())

    check_list[input_num] = check_list[input_num] + 1

for i in range(10001): # 만약 check_list로 넣게 될 경우에 0으로 되기때문에 성립이 안됨
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)


#4

import sys
from collections import Counter

# main
t = int(sys.stdin.readline())

numbers = []

for _ in range(t):
    numbers.append(int(sys.stdin.readline()))

def mean(nums):
    return round(sum(nums)/len(nums))


def median(nums):
    nums.sort()
    mid = nums[len(nums)//2] # nums의 개수는 홀 수

    return mid

def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()

    if len(nums) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0] # 이경우에는 앞에 있는 최빈값만 나타 낼 수 있다. ex) (4, 2) / 4
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]

    return mod


def scope(nums):
    return max(nums) - min(nums)

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(scope(numbers))


# 5

n = int(input())


li = list(map(int, str(n)))

li.sort(reverse=True)

for i in li:
    print(i,end='')


# 6

n = int(input())

nums = []

for i in range(n):
    [x, y] = map(int, input().split())
    nums.append([x, y])

nums = sorted(nums)

for i in range(n):
    print(nums[i][0], nums[i][1])


#7

import sys

input = sys.stdin.readline

n = int(input())

a = []

for i in range(n):
    [x, y] = map(int, input().split())
    rev = [y, x]
    a.append(rev)

b = sorted(a)

for i in range(n):
    print(b[i][1], b[i][0])


#8

import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst)
lst = list(set_lst)
lst.sort()
lst.sort(key = len)


for i in lst:
    print(i)


#9

import sys

n = int(sys.stdin.readline())

member = []

for i in range(n):
    member.append(list(sys.stdin.readline().split()))
member.sort(key = lambda x: int(x[0]))

for i in range(n): #
    print(member[i][0], member[i][1])


#10 youtube

import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr2 = sorted(list(set(arr)))

dic = {arr2[i] : i for i in range(len(arr2))}

for i in arr:
    print(dic[i], end = ' ')