def key_value(sentence):
    freq = {}
    
    for char in sentence:
        if char != " ":   # exclude spaces
            freq[char] = freq.get(char, 0) + 1
    
    return freq


sentence = input("Enter a sentence: ")
result = key_value(sentence)
print("Character frequency:", result)