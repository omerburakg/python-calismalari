word = input()
word = word.lower()
sesli = ["a", "e", "i", "o", "u"]
letters_list = [i for i in word if i not in sesli]
print(letters_list)
