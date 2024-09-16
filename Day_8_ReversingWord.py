def reverse_words(s):
    s = s.strip()
    words = []
    word = []
    
    for char in s:
        if char != ' ':
            word.append(char)
        else:
            if word:
                words.append(''.join(word))
                word = []
    
    if word:
        words.append(''.join(word))

    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])

    return ' '.join(reversed_words)

s = input("Enter the string: ")
result = reverse_words(s)
print(f"Reversed string: '{result}'")
