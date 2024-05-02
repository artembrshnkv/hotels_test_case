def find_common_divisors(numbers: list[int]) -> list[int]:
    min_number = min(numbers)
    common_divisors = []

    for i in range(1, min_number + 1):
        if all(num % i == 0 for num in numbers):
            common_divisors.append(i)

    return common_divisors


if __name__ == '__main__':
    print(find_common_divisors([42, 12, 18]))
