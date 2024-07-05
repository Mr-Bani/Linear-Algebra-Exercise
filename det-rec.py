def get_matrix_minor(matrix, i, j):
    # حذف سطر i و ستون j از ماتریس
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def calculate_determinant(matrix):
    # اگر ماتریس یک عنصره باشد، دترمینان برابر با همان عنصر است
    if len(matrix) == 1:
        return matrix[0][0]

    # اگر ماتریس 2x2 باشد، دترمینان به صورت ساده محاسبه می‌شود
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1)**c) * matrix[0][c] * calculate_determinant(get_matrix_minor(matrix, 0, c))
    return determinant

def main():
    n = int(input())
    matrix = []
    for i in range(n):
        data = list(input().split())
        row = []
        for j in range(n):
            row.append(float(data[j]))
        matrix.append(row)
    determinant = calculate_determinant(matrix)
    print(f"{determinant:.2f}")

main()
