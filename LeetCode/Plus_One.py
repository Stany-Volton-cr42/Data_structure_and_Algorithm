digits = [9,9,9,9]

# Sorting the digits in descending order
for i in range(len(digits) -1, -1, -1):
    if digits[i] == 9:
        digits[i] = 0
    else:
        digits[i] += 1
        print(digits)
        break
else:
    digits = [0] * (len(digits) + 1)
    digits[0] = 1
    print(digits)


# Time Complexity: O(n)
"With the function"

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         for i in range(len(digits) - 1, -1, -1):
#             if digits[i] == 9:
#                 digits[i] = 0
#             else:
#                 digits[i] += 1
#                 return digits
        
#         digits = [0] * (len(digits) + 1)
#         digits[0] = 1
#         return digits
    
# # call the function

# solution = Solution()
# print(solution.plusOne([1, 2, 3]))

# # Space Complexity: O(1)

