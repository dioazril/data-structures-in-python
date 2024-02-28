# Intuition

The first thought that comes to mind for this problem is to check if any element appears more than once in the array. We can achieve this by keeping track of the elements we have already seen.

# Approach

One approach is to use a set to store the unique elements encountered while iterating through the array. Sets inherently do not allow duplicates. If the length of the original array and the set after iterating through the array are not the same, it means there were duplicates, and we can return True. Otherwise, all elements were unique, and we can return False.

# Complexity

## Time complexity:

O(n)
(linear). This is because we iterate through the entire array once using a loop.

## Space complexity:

O(n)

(linear). We use a set to store unique elements encountered during iteration, which can potentially hold all elements in the worst case.
