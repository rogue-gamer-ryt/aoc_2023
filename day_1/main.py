input = open("input", "r")
res = 0

alpha_to_int = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_digits(sentence):
    words = []
    curr_str = ""
    for char in sentence:
        curr_str += char
        if char.isnumeric():
            words += char
            curr_str = ""
        else:
            for j in alpha_to_int:
                if j in curr_str:
                    words += str(alpha_to_int[j])
                    curr_str = curr_str[len(curr_str)-len(j):]
    print(words)
    return words


for sentence in input:
    digits = get_digits(sentence=sentence)
    number = int(str(digits[0]) + str(digits[-1]))
    res += number
    print(number)
print(res)

