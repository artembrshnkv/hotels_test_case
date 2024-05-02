def is_prime(n: int) -> bool:
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def find_prime_numbers_in_range(min_number: int,
                                max_number: int) -> list[int]:
    prime_numbers_array = []
    for number in range(min_number, max_number + 1):
        if is_prime(number):
            prime_numbers_array.append(number)

    return prime_numbers_array


if __name__ == '__main__':
    print(find_prime_numbers_in_range(11, 20))
