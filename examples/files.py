with open("decrypt.txt", "r") as f:
    for line in f:
        stripped = line.strip()
        # print(stripped)


s='what ever '
print(s[3:])
result =''
for ch in s:
    result += ch
# print(result)


def unfold(word):
    if len(word) == 0:
        return ''
    elif len(word) == 1:
        return word
    else:
        return word[0] + unfold(word[1:]) + word[0]

print(unfold('rota'))