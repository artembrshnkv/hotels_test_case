def draw_multiplication_table(n: int) -> None:
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 1):
            row += f"{i * j:3}"

        print(row)


if __name__ == '__main__':
    draw_multiplication_table(5)
