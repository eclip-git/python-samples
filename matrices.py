matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[3, 2, 3, 5], [4, 5, 6, 7]]


def madd(m1, m2):

    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        print("matrices different dimensions")
        return
    m3 = []
    m3row = []
    for i in range(0, len(m1)):
        for j in range(0, len(m1[i])):
            m3row.append(m1[i][j] + m2[i][j])
        m3.append(m3row)
        m3row = []

    return m3


print(matrix1)
print(matrix2)
print(madd(matrix1, matrix2))
