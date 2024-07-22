
## 26. Remove Duplicates from Sorted Array

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The relative order of the elements should be kept the same. Then return *the number of unique elements in `nums`*.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:
- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

### Custom Judge:
The judge will test your solution with the following code:
```cpp
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be accepted.

### Example 1:
**Input:** nums = [1,1,2]  
**Output:** 2, nums = [1,2,_]  
**Explanation:** Your function should return `k = 2`, with the first two elements of `nums` being 1 and 2 respectively. It does not matter what you leave beyond the returned `k` (hence they are underscores).

### Example 2:
**Input:** nums = [0,0,1,1,1,2,2,3,3,4]  
**Output:** 5, nums = [0,1,2,3,4,_,_,_,_,_]  
**Explanation:** Your function should return `k = 5`, with the first five elements of `nums` being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned `k` (hence they are underscores).

### Constraints:
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing** order.

---
`
---





# Explanation of the Code

Let's break down the code step by step and explain the concept in simple, easy-to-understand words:

---

**Problem:**
You are given a sorted array `nums`. Your task is to remove duplicates in-place such that each element appears only once and returns the new length of the array. The relative order of the elements should be kept the same, and you must do this with constant extra space.

**Code:**
```python
if not nums:
    return 0

j = 0
for i in range(1, len(nums)):
    if nums[j] != nums[i]:
        j += 1
        nums[j] = nums[i]

return j + 1
```

---

**Concept:**

1. **Handling Empty Array:**
   - `if not nums:` checks if the array `nums` is empty.
   - If `nums` is empty, it returns `0` immediately because there are no elements to process.

2. **Initializing the Pointer `j`:**
   - `j = 0` initializes a pointer `j` to the first element of the array.
   - This pointer `j` will help track the position where the next unique element should be placed.

3. **Looping Through the Array:**
   - `for i in range(1, len(nums)):` starts a loop from the second element (index `1`) to the end of the array.
   - This loop will check each element to see if it is a duplicate.

4. **Checking for Duplicates:**
   - `if nums[j] != nums[i]:` compares the current element `nums[i]` with the last unique element `nums[j]`.
   - If they are not the same, it means `nums[i]` is a new unique element.

5. **Updating the Array with Unique Elements:**
   - `j += 1` increments the pointer `j` to move to the next position.
   - `nums[j] = nums[i]` places the new unique element at the updated position `j`.

6. **Returning the Length of the New Array:**
   - `return j + 1` returns the new length of the array.
   - Since `j` is the index of the last unique element, the length is `j + 1`.

**Example:**

Let's take an example array to understand the output:

```python
nums = [1, 1, 2, 2, 3, 4, 4, 5]
```

1. **Initial Array:**
   - `nums` = [1, 1, 2, 2, 3, 4, 4, 5]

2. **First Iteration (`i = 1`):**
   - `nums[0]` is compared with `nums[1]` (both are 1).
   - They are the same, so we move to the next iteration without any changes.

3. **Second Iteration (`i = 2`):**
   - `nums[0]` is compared with `nums[2]` (1 vs. 2).
   - They are different, so `j` is incremented to 1 and `nums[1]` is set to 2.
   - Updated `nums` = [1, 2, 2, 2, 3, 4, 4, 5]

4. **Continuing the Iterations:**
   - The loop continues, comparing and updating the array with unique elements.
   - After all iterations, `nums` = [1, 2, 3, 4, 5, 4, 4, 5] and `j = 4`.

5. **Returning the Length:**
   - `return j + 1` returns 5, which is the new length of the array with unique elements.

**Final Array:**
- The first 5 elements of the array are now unique: [1, 2, 3, 4, 5].

---

**Summary:**
The code efficiently removes duplicates from a sorted array in-place by using a pointer `j` to track the position of unique elements. It ensures that each unique element is moved to the front of the array, and returns the new length of the array without duplicates.

I hope this explanation helps clarify how the code works!