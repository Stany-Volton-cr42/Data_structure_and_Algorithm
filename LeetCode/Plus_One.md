## 66. Plus One

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the i<sup>th</sup> digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return the resulting array of digits.

### Example 1:
**Input:** digits = [1,2,3]  
**Output:** [1,2,4]  
**Explanation:** The array represents the integer 123. Incrementing by one gives 123 + 1 = 124. Thus, the result should be [1,2,4].

### Example 2:
**Input:** digits = [4,3,2,1]  
**Output:** [4,3,2,2]  
**Explanation:** The array represents the integer 4321. Incrementing by one gives 4321 + 1 = 4322. Thus, the result should be [4,3,2,2].

### Example 3:
**Input:** digits = [9]  
**Output:** [1,0]  
**Explanation:** The array represents the integer 9. Incrementing by one gives 9 + 1 = 10. Thus, the result should be [1,0].

### Constraints:
- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` does not contain any leading `0`'s.
---
---
___
``
____________________________________________________________
### Explanation of the Code

Let's break down the code step by step and explain the concept in simple and easy-to-understand words:


**Question:**
You are given a list of digits representing a non-negative integer. You need to add one to the integer and return the resulting list of digits.

**Code:**

```python
def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    
    digits = [0] * (len(digits) + 1)
    digits[0] = 1
    return digits
```

---

**Concept:**

1. **Understanding the Problem:**
   - We have a number represented as a list of digits. For example, the number `123` is represented as `[1, 2, 3]`.
   - We need to add one to this number and return the resulting number as a list of digits.

2. **Iterating from the End:**
   - The `for` loop starts from the last digit of the list and moves backward to the first digit:
     ```python
     for i in range(len(digits) - 1, -1, -1):
     ```
   - This is because adding one usually affects the least significant digit (the rightmost one) first.

3. **Handling Nines:**
   - If the current digit is `9`, adding one makes it `10`. Instead of writing `10`, we set the current digit to `0` and carry over `1` to the next digit to the left:
     ```python
     if digits[i] == 9:
         digits[i] = 0
     ```
   - This is like resetting the current digit and moving the addition to the next place value.

4. **No Carry Case:**
   - If the current digit is not `9`, we simply add one to this digit and return the updated list:
     ```python
     else:
         digits[i] += 1
         return digits
     ```
   - This is because no further changes are needed if there is no carry.

5. **All Nines Case:**
   - If all digits are `9`, like `999`, after the loop ends, all digits will be `0` due to the carry over:
     ```python
     digits = [0] * (len(digits) + 1)
     digits[0] = 1
     ```
   - We create a new list with an extra digit set to `1` at the beginning, representing the carry-over for an all-9s list (e.g., `999` becomes `1000`).

**Example:**

Let's take an example list to see what happens:

```python
digits = [1, 2, 9]
```

1. **Iterating from the End:**
   - Start from the last digit: `9`.

2. **Handling Nine:**
   - `9` becomes `0` and carry over `1` to the next digit.
   - The list is now `[1, 2, 0]`.

3. **Next Digit:**
   - Move to the next digit: `2`.
   - `2` becomes `3` (adding the carry over).

4. **Returning the Result:**
   - The list is now `[1, 3, 0]`.
   - Return the updated list.

5. **Another Example:**
   - For input `[9, 9, 9]`:
     - All digits become `0`.
     - Create a new list `[1, 0, 0, 0]`.

**Summary:**
The code effectively adds one to any number represented as a list of digits by handling carries correctly. It iterates from the end of the list, handles cases where digits are `9`, and creates a new list if all digits are `9`.

I hope this explanation makes the code easy to understand!
