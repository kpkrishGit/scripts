def count_vowels(sentence:str):
    """
    find vowel count in a sentence
    We are not initializing a vowels_count with each vowel set to 0
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_cnt = {}
    for char in sentence:
        if char in vowels:
            vowel_cnt.setdefault(char, 0)
            vowel_cnt[char] += 1
    return(vowel_cnt)
