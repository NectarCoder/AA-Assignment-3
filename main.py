"""
PSEUDOCODE

Below is the pseudocode for the Levenshtein algorithm:
function levenshtein_distance(word1, word2) returns difference:
    matrix = new matrix(rows = word1.length+1, cols = word2/length+1)
    for matrix.numberOfRows:
        matrix[m][0] = m

    for matrix.numberOfCols:
        matrix[0][n] = n

    row index i = 0
    column index j = 0
    for every cell in matrix from (1,1) to (m,n):
        if word1.character(i-1) == word2.character(j-1):
            matrix[i][j] = matrix[i-1][j-1] (value of cell diagonally above to the left)
        else:
            matrix[i][j] = minimum value of the following set:
                        matrix[i-1][j] + 1 (value of cell above)
                        matrix[i][j-1] + 1 (value of cell to the left)
                        matrix[i-1][j-1] + 1 (value of cell diagonally above to the left)

    return matrix[m][n] (value of the cell in the last row and last column)
"""

"""
BELLMAN-EQUATIONS

The Bellman-Equation piecewise function is shown in the README.md file.
Please review that.

"""


def levenshtein_distance(word1, word2):
    # First we initialize a matrix with dimensions (len(word1)+1) x (len(word2)+1)
    matrix = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    '''
    We initialize the first row and first column of the matrix with (1,2,3,...,n) - as this is a constant value in the Levenshtein algorithm.
    Regardless of the difference of the input words.
    '''
    # Initialize the first row of the matrix
    for i in range(len(word1) + 1):
        matrix[i][0] = i

    # Initialize the first column of the matrix
    for j in range(len(word2) + 1):
        matrix[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                # If the characters at the current positions are equal, no operation needed,
                # take the value from the diagonal (top-left) cell
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                # If characters are not equal, choose the minimum cost among deletion, insertion, and substitution
                # and set that min value for the current cell
                matrix[i][j] = 1 + min(
                    matrix[i - 1][j],  # Deletion
                    matrix[i][j - 1],  # Insertion
                    matrix[i - 1][j - 1]  # Substitution
                )

    # Return the bottom-right cell of the matrix, which contains the Levenshtein distance
    return matrix[len(word1)][len(word2)]


def main():
    input_file = "InputsOutputs\\Input.txt"
    output_file = "InputsOutputs\\Output.txt"

    with open(input_file, "r") as input, open(output_file, "w") as output:
        for line in input:
            values = line.strip().split(",")

            if len(values) == 2:
                word1, word2 = values
                output_line = "{},{},{}".format(word1, word2, levenshtein_distance(word1, word2))
                print(output_line, file=output)
            else:
                print("Error!")

    print("OUTPUT FILE CONTENTS: ")
    print()

    with open(output_file, "r") as output:
        for line in output:
            print(line.strip())


main()
