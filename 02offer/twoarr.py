

class Solution:

    def find(self, target,  array):
        if not array:
            return

        row = len(array)
        col = len(array[0])

        for i in range(row):
            for j in range(col):
                if target == array[i][j]:
                    return True

        return False


# o(n^2)