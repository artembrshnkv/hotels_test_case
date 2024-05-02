def declension_of_word_computer(number: int) -> str:
    last_digit = number % 10
    last_two_digits = number % 100


    if 11 <= last_two_digits <= 19:
        response = "компьютеров"
    elif last_digit == 1:
        response = "компьютер"
    elif 2 <= last_digit <= 4:
        response = "компьютера"
    else:
        response = "компьютеров"

    return f"{number} {response}"


if __name__ == '__main__':
    print(declension_of_word_computer(1))

