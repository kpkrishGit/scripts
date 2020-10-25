'''
find vowel count in a sentence
We are not initializing a vowels_count with each vowel set to count 0
'''
st = 'Here is a sample sentence'
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_cnt = {}
for char in st:
    if char in vowels:
        vowel_cnt.setdefault(char, 0)
        vowel_cnt[char] += 1
print(vowel_cnt)
