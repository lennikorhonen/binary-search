import random
import math

# TODO: Make it recognize duplicates

# num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
num = []

for x in range(100):
    num.append(random.randint(1,100))

num.sort()

def binary_search(target):
    # num, len(num), T == A, n, T
    #T = input("Search number: ")
    #T = int(T)
    left = 0
    right = len(num) - 1
    print(num)
    print('num length', len(num))
    while left <= right:
        mid = math.floor((left + right)/2)
        if num[mid] < target:
            left += 1
        elif num[mid] > target:
            right -= 1
        else:
            return m
    print("Not found on list")

# binary_search(40)
