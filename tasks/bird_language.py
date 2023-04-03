import re
# после гласных еще 2 гласных, после согласных 1 символ

def translate(text: str) -> str:
    text_tr = re.sub(r'([aeiouy])\1\1', r'\1', text)
    text_tr_2 = re.sub(r'([^aeiouy ])[aeiouy]', r'\1', text_tr)

    return text_tr_2


print("Example:")
print(translate("hieeelalaooo"))
print(translate("sooooso aaaaaaaaa"))
print(translate("aaa bo cy da eee fe"))
print(translate("hoooowe yyyooouuu duoooiiine"))

# These "asserts" are used for self-checking
assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")
