import pyperclip

input = input("Please input some text:\n")

exceptions = ["a","an","the","and","as","but","for","if","nor", "or", "so", "yet"] 

result = []
words = input.lower().split()


for word in words:
    if word.isalpha() and word not in exceptions:
        cap = word.capitalize()
        result.append(cap)
    else:
        result.append(word)

answer = " ".join(result)
print(answer)

pyperclip.copy(answer)

print("Copied to Clipboard",)
