# Remove all duplicates words from a given sentence


def removeDuplicateWords(sentence: str) -> str:
    words = sentence.split()
    unique_words = {}
    result = []

    for word in words:
        if word not in unique_words:
            unique_words[word] = True
            result.append(word)

    return " ".join(result)


sentence = "hello world world is beautiful world"
result = removeDuplicateWords(sentence)
print(result)
