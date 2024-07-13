# Alternates in an Array

**Difficulty:** School  
**Accuracy:** 52.74%  
**Submissions:** 180K+  
**Platform:**  GeeksforGeeks

You are given an array `arr`. You need to print elements of `arr` in alternate order (starting from index 0).

### Examples:

**Input:** `arr[] = [1, 2, 3, 4]`  
**Output:** `1 3`

**Input:** `arr[] = [1, 2, 3, 4, 5]`  
**Output:** `1 3 5`

**Expected Time Complexity:** O(n)  
**Expected Space Complexity:** O(1)

### Constraints:
- `1 <= arr.size <= 10^5`
- `1 <= arr[i] <= 10^5`


---
___
``
____________________________________________________________
- # Answer and Explaination of the code

### Explanation of the Code

Let's break down the code step by step and explain the concept in simple and easy-to-understand words:

---

**Question:**
You have an array `arr`. You need to print elements of `arr` in an alternate order (starting from index 0).

**Code:**
```python
for i in arr[::2]:
    print(i, end=" ")
```

---

**Concept:**

1. **Understanding Slicing:**
   - `arr[::2]` is a way to pick elements from the array `arr` with a fixed interval.
   - Let's break it down:
     - `arr[start:end:step]` is the general form.
     - `start`: Where to start (default is the beginning of the array).
     - `end`: Where to stop (default is the end of the array).
     - `step`: How many steps to take each time (in this case, 2).

   So, `arr[::2]` means "start at the beginning, go till the end, and pick every second element."

2. **Looping Through the Sliced Array:**
   - `for i in arr[::2]:` means we are going through each element in the array created by `arr[::2]`.
   - For example, if `arr` is `[1, 2, 3, 4, 5]`, then `arr[::2]` results in `[1, 3, 5]`.

3. **Printing the Elements:**
   - `print(i, end=" ")` means we print each element `i` followed by a space instead of a newline.
   - The `end=" "` argument in the `print` function ensures that each printed element is followed by a space.

**Example:**

Let's take an example array to see what happens:

```python
arr = [47, 6, 46, 17, 11, 29, 60, 31, 9]
```

1. **Slicing the Array:**
   - `arr[::2]` results in `[47, 46, 11, 60, 9]`.

2. **Looping and Printing:**
   - The loop goes through the sliced array `[47, 46, 11, 60, 9]`.
   - It prints each element followed by a space:
     ```
     47 46 11 60 9
     ```

---

**Summary:**
The code prints every alternate element of the array starting from index 0, ensuring the output is in a single line with space-separated values. This approach is both simple and effective, using Python's slicing feature.

