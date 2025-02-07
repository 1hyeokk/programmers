import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().strip().split()))
num_filter = sorted(set(num_list))

num_rate = {num_filter[i] : i for i in range(len(num_filter))}

for i in num_list:
    print(num_rate[i], end = ' ')