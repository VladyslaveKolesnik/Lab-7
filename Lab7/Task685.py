import math
def check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
def triangle(a, b, c):
    if check(a, b, c) == False:
        print("triangle does not exist")
    else:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"{s:.2f}")
def circle(r):
    s = 3.14 * r ** 2
    print(f"{s:.2f}")
def rectangle(a, b):
    s = a * b
    print(f"{s:.2f}")
def solve(name, nums):
    if name == "triangle":
        triangle(nums[0], nums[1], nums[2])
    elif name == "circle":
        circle(nums[0])
    elif name == "rectangle":
        rectangle(nums[0], nums[1])
while True:
    try:
        name = input()
        if name == "":
            break
        line = input()
        str_list = line.split()
        nums = []
        for x in str_list:
            nums.append(float(x))
        solve(name, nums)
    except:
        break