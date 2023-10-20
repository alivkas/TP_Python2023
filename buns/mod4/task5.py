with open("input", 'r') as input_file:
    text = input_file.read()
    letter_count = {}

    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1])
    with open("result.txt", "w") as result_file:
        for letter, count in sorted_letter_count:
            result_file.write(f"{letter}: {str(count)} \n")