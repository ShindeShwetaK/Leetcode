class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        r = 0
        c = n - 1

        while r < m and c >=0:
            if matrix[r][c] > target:
                c -= 1

            elif matrix[r][c] < target:
                r += 1

            else:
                return True

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if target == matrix[i][j]:
                    return True

        return False


#######################################################

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = 0
        l = len(nums) - 1

        while r <= l:
            mid = r + ((l - r) //2)

            if target == nums[mid]:
                return mid

            elif nums[mid] > target:
                l = mid - 1

            else:
                r  = mid + 1

        return -1






        
