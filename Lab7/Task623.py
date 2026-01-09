def find_min_max(numbers):
    return min(numbers), max(numbers)

data = list(map(int, input().split()))
print(find_min_max(data))