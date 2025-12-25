904. Fruit Into Baskets
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        unique = {}
        l = 0
        max_len = 0

        for r, n in enumerate(fruits):
            if n not in unique:
                unique[n] = 1
            else:
                unique[n] += 1


            while len(unique) > 2:
                unique[fruits[l]] -= 1
                if unique[fruits[l]] == 0:
                    del unique[fruits[l]]
                l += 1

            max_len = max(max_len, r - l + 1)


        return max_len

------------------------------------------------------------------
713. Subarray Product Less Than K
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if  k <= 1:
            return 0

        l = 0
        max_nums = 0
        curr_mul = 1

        for r in range(len(nums)):
            curr_mul *= nums[r]

            while curr_mul >= k:
                curr_mul //= nums[l]
                l += 1

            max_nums += r - l + 1

        return max_nums

        



            

            

            
        
