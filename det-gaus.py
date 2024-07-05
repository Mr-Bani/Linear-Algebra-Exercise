def gauss_jordan_determinant(matrix):
    n = len(matrix)
    det = 1
    for i in range(n):
        # پیدا کردن بزرگترین عنصر در ستون برای استفاده به عنوان محور
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k

        # تعویض سطرها اگر محور اصلی صفر است
        if i != max_row:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            det *= -1

        # اگر محور صفر است، دترمینان صفر است
        if matrix[i][i] == 0:
            return 0

        # حذف گاوسی برای ایجاد ماتریس مثلثی
        for k in range(i + 1, n):
            factor = matrix[k][i] / matrix[i][i]
            for j in range(i, n):
                matrix[k][j] -= factor * matrix[i][j]

        # ضرب عناصر روی قطر اصلی
        det *= matrix[i][i]

    return det


def main():
    n = int(input())
    matrix = []
    for i in range(n):
        data = list(input().split())
        row = []
        for j in range(n):
            row.append(float(data[j]))
        matrix.append(row)

    determinant = gauss_jordan_determinant(matrix)
    print(f"{determinant:.2f}")


if __name__ == "__main__":
    main()
