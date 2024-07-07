# Min and Max in Array

Given an array `arr`. Your task is to find the **minimum** and **maximum** elements in the array.

**Note:** Return an array that contains two elements. The first one will be the minimum element and the second will be the maximum of an array.

### Examples:

**Input:** `arr = [3, 2, 1, 56, 10000, 167]`  
**Output:** `1 10000`  
**Explanation:** The minimum and maximum elements of the array are `1` and `10000`.

**Input:** `arr = [1, 345, 234, 21, 56789]`  
**Output:** `1 56789`  
**Explanation:** The minimum and maximum elements of the array are `1` and `56789`.

**Input:** `arr = [56789]`  
**Output:** `56789 56789`  
**Explanation:** Since the array contains only one element, both min & max are the same.

**Expected Time Complexity:** O(n)  
**Expected Auxiliary Space:** O(1)

### Constraints:
- `1 <= arr.size() <= 10^5`
- `1 <= arr[i] <= 10^12`
