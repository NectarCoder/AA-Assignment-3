def levenshtein_distance(word1, word2):
    # Initialize a matrix with dimensions (len(word1)+1) x (len(word2)+1)
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    # Initialize the first row and column of the matrix
    for i in range(len(word1) + 1):
        dp[i][
            0] = i  # Each cell in the first column represents the cost of deleting characters from word1 to make it empty

    for j in range(len(word2) + 1):
        dp[0][
            j] = j  # Each cell in the first row represents the cost of inserting characters into word1 to make it equal to word2

    # Fill in the rest of the matrix
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                # If the characters at the current positions are equal, no operation needed,
                # take the value from the diagonal (top-left) cell
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # If characters are not equal, choose the minimum cost among deletion, insertion, and substitution
                dp[i][j] = 1 + min(
                    dp[i - 1][j],  # Deletion
                    dp[i][j - 1],  # Insertion
                    dp[i - 1][j - 1]  # Substitution
                )

    # Return the bottom-right cell of the matrix, which contains the Levenshtein distance
    return dp[len(word1)][len(word2)]


# Example usage:
word1 = "abcd"
word2 = "wxyzlmnop"
print("Levenshtein distance between '{}' and '{}': {}".format(word1, word2, levenshtein_distance(word1, word2)))
