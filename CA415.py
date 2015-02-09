def anti_vowel(text):
    no_vowel = ""
    for item in text:
        if item not in "aeiouAEIOU":
           no_vowel = no_vowel + item
    return no_vowel    

print anti_vowel('text')