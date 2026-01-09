def insert_middle(str1, str2):
    mid = len(str1) // 2
    return str1[:mid] + str2 + str1[mid:]

while True:
    try:
        line = input()
        if not line: break
        s1, s2 = line.split()
        print(insert_middle(s1, s2))
    except ValueError:
        break
