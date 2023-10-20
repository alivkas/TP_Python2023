def find_palindrome(word):
    char_count = {}

    for char in word:
        char_count[char] = char_count.get(char, 0) + 1

    palindrome_half = []
    middle_char = None

    for char, count in char_count.items():
        if count % 2 != 0:
            if middle_char is not None:
                return None
            middle_char = char

        palindrome_half.extend([char] * (count // 2))

    palindrome = ''.join(palindrome_half) + (middle_char or '') + ''.join(palindrome_half[::-1])
    return palindrome


word = input('Введите слово: ')
palindrome = find_palindrome(word)
if palindrome is not None:
    print(f'Палиндром, составленный из слова "{word}": {palindrome}')
else:
    print(f'Из слова "{word}" невозможно составить палиндром')