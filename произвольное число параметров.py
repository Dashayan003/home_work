def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()
    for word in other_words:
        if root_word_lower in word.lower():
            same_words.append(word)
    return same_words
result = single_root_words('able', 'Disablement', 'Able', 'abLe', 'example', 'ability')
print(result)