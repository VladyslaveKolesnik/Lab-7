def capitalize_word(word):
    return word.title()

words = input().split()
print(" ".join([capitalize_word(word) for word in words]))