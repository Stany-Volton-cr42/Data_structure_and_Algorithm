    

# if not nums:
#         return 0
    
# j = 0
# for i in range(1, len(nums)):
#     if nums[j] != nums[i]:
#         j += 1
#         nums[j] = nums[i]
    
# return j + 1



nums = [1, 1, 2,2,2,2,3,3,3,4]  # Example array, you can replace it with your array

# Check if the array is empty
if not nums:
    new_length = 0
else:
    j = 0
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the element at index `j`
        if nums[j] != nums[i]:
            # Increment `j` and update the element at index `j`
            j += 1
            nums[j] = nums[i]
    # The new length of the array is `j + 1`
    new_length = j + 1

print("New length of the array:", new_length)
print("Updated array without duplicates:", nums[:new_length])
