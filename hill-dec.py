def get_matrix_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

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

def matrix_mod_inverse(matrix, modulus):
    n = len(matrix)
    determinant = calculate_determinant(matrix)
    determinant = determinant % modulus
    determinant_inv = mod_inverse(determinant, modulus)
    if determinant_inv == -1:
        return None

    cofactors = []
    for r in range(n):
        cofactor_row = []
        for c in range(n):
            minor = get_matrix_minor(matrix, r, c)
            cofactor_row.append(((-1) ** (r + c)) * calculate_determinant(minor))
        cofactors.append(cofactor_row)

    for r in range(n):
        for c in range(r, n):
            cofactors[r][c], cofactors[c][r] = cofactors[c][r], cofactors[r][c]

    for r in range(n):
        for c in range(n):
            cofactors[r][c] = (cofactors[r][c] * determinant_inv) % modulus
            cofactors[r][c] = cofactors[r][c] % modulus

    return cofactors

def hill_cipher_decrypt(key_matrix, text):
    n = len(key_matrix)
    key_matrix_inv = matrix_mod_inverse(key_matrix, 27)
    if key_matrix_inv is None:
        return "NO_VALID_KEY"

    text_numbers = [ord(char) - ord('A') if char != '_' else 26 for char in text]
    plain_numbers = []

    for i in range(0, len(text_numbers), n):
        block = text_numbers[i:i+n]
        plain_block = [0] * n
        for row in range(n):
            for col in range(n):
                plain_block[row] += key_matrix_inv[row][col] * block[col]
            plain_block[row] = plain_block[row] % 27
        plain_numbers.extend(plain_block)

    plain_text = ''.join(chr(num + ord('A')) if num != 26 else '_' for num in plain_numbers)
    return plain_text

def main():
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    text = input().strip()
    plain_text = hill_cipher_decrypt(matrix, text)
    print(plain_text)

if __name__ == "__main__":
    main()
