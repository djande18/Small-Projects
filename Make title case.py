import pyperclip

input = input("Please input some text:\n")

result = []
words = input.split()

for word in words:
    if word.isalpha():
        cap = word.capitalize()
        result.append(cap)
    else:
        result.append(word)

answer = " ".join(result)
print(answer)

pyperclip.copy(answer)

print("Copied to Clipboard",)
