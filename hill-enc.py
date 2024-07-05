def get_matrix_minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def calculate_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1) ** c) * matrix[0][c] * calculate_determinant(get_matrix_minor(matrix, 0, c))
    return determinant


def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1


def hill_cipher_encrypt(key_matrix, text):
    n = len(key_matrix)
    text = text.replace(' ', '_').upper()
    while len(text) % n != 0:
        text += '_'

    # تبدیل حروف به اعداد
    text_numbers = [ord(char) - ord('A') if char != '_' else 26 for char in text]
    cipher_numbers = []

    for i in range(0, len(text_numbers), n):
        block = text_numbers[i:i + n]
        cipher_block = [0] * n
        for row in range(n):
            for col in range(n):
                cipher_block[row] += key_matrix[row][col] * block[col]
            cipher_block[row] = cipher_block[row] % 27
        cipher_numbers.extend(cipher_block)

    # تبدیل اعداد به حروف
    cipher_text = ''.join(chr(num + ord('A')) if num != 26 else '_' for num in cipher_numbers)
    return cipher_text


def main():
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    determinant = calculate_determinant(matrix) % 27
    if determinant == 0 or mod_inverse(determinant, 27) == -1:
        print("NO_VALID_KEY")
        return

    text = input().strip()
    cipher_text = hill_cipher_encrypt(matrix, text)
    print(cipher_text)


if __name__ == "__main__":
    main()
