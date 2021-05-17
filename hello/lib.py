def try_me(word1, word2):
    if len(word1) > len(word2):
        return f"{word1} is longer than {word2}"
    elif len(word1) < len(word2):
        return f"{word1} is longer than {word2}"
    else:
        return f"{word1} and {word2} have the same length"