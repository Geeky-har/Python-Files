def matrix(m, n):
    final = []
    for i in range(m):
        row = []
        for j in range(n):
            value = int(input())
            row.append(value)
        final.append(row)

    return final

def sum(A, B):
    final = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            value = A[i][j] + B[i][j]
            row.append(value)
        final.append(row)

    return final


if __name__ == '__main__':

    m = int(input("Enter the number of rows in the matrix: "))

    n = int(input("Enter the number of columns in the matrix: "))

    print("Enter the values of first matrix: \n")

    A = matrix(m, n)

    print("Enter the values of second matrix: \n")

    B = matrix(m, n)

    S = []

    S = sum(A, B)

    print('The resultant matrix after the sum is: ')

    for i in range(m):
        row = []
        for j in range(n):
            print(S[i][j], end = ' ')
        print()
