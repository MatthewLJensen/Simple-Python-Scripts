mat1 = [[1.5, 0.2 , 3],
        [4, 2.5, 8]]
mat2 = [[1, 5.6],
        [4.3, 0.53],
        [11, 7]]

mat3 = [[-5, 3, -7],
        [3, -2, 5]]
mat4 = [[10, 6, -7, 1],
        [-8, -9, -1, 9],
        [0, -2, 7, 5]]


def matrix_multiply(matrix1, matrix2):
    """
    >>> matrix_multiply([[-5, 3, -7], [3, -2, 5]],[[10, 6, -7, 1],[-8, -9, -1, 9],[0, -2, 7, 5]])
    [[-74, -43, -17, -13], [46, 26, 16, 10]]
    
    >>> matrix_multiply([[1],[2],[3]],[[1,2,3]])
    [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    
    >>> len(matrix_multiply([[1,2,3]], [[1],[2],[3]]))
    1
    
    >>> len(matrix_multiply([[1],[2],[3]],[[1,2,3]]))
    3
    """
    answer = [[] for i in range(len(matrix1))]
    for row in range(len(matrix1)):
        for id in range(len(matrix2[0])):
            sum = 0
            for row2 in range(len(matrix2)):
                    sum += matrix1[row][row2] * matrix2[row2][id]
            answer[row].append(sum)
    return answer
    

import doctest
doctest.testmod()