def censor(text, word):
    new_word = "*" * len(word)
    text = text.split()
    new_text = []
    for item in text:
        if item == word:
            new_text.append(new_word)
        else:
            new_text.append(item)
       return " ".join(new_text)
        