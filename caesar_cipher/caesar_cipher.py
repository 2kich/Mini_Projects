from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(message: str, shift_order: int, cipher_direction: str):
    result = ""
    if cipher_direction == "decode":
        shift_order *= -1
    for ch in message:
        if ch not in alphabet:
            result += str(ch)
        else:
            idx = alphabet.index(ch)
            result += alphabet[idx + shift_order]
    print(f"The {cipher_direction}d text is {result}")


print(logo)


restart = True

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    n = len(alphabet)

    caesar(text, shift, direction)
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if repeat == "no":
        restart = False
