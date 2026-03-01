#!/usr/bin/env python3
"""
DSA Arrays Tutorial - Complete Guide for Beginners
==================================================

This tutorial covers:
1. What are arrays
2. Array creation and basic operations
3. Common array problems and solutions
4. Time and space complexity analysis
"""

# =============================================================================
# 1. WHAT ARE ARRAYS?
# =============================================================================

"""
An array is a collection of elements stored in contiguous memory locations.
Each element can be accessed using its index.

Key characteristics:
- Fixed size (in most languages)
- Elements are of the same data type
- Index starts from 0
- Random access in O(1) time
"""

print("=" * 50)
print("1. ARRAY BASICS")
print("=" * 50)

# Creating arrays in Python (using lists)
arr1 = [1, 2, 3, 4, 5]  # Integer array
arr2 = ['a', 'b', 'c', 'd']  # Character array
arr3 = [1.5, 2.7, 3.9]  # Float array
arr4 = [True, False, True]  # Boolean array

print(f"Integer array: {arr1}")
print(f"Character array: {arr2}")
print(f"Float array: {arr3}")
print(f"Boolean array: {arr4}")

# Array with mixed types (Python allows this, but not recommended for DSA)
mixed_arr = [1, 'hello', 3.14, True]
print(f"Mixed array (not recommended): {mixed_arr}")

# =============================================================================
# 2. BASIC ARRAY OPERATIONS
# =============================================================================

print("\n" + "=" * 50)
print("2. BASIC ARRAY OPERATIONS")
print("=" * 50)

# Accessing elements
arr = [10, 20, 30, 40, 50]
print(f"Original array: {arr}")
print(f"Element at index 0: {arr[0]}")
print(f"Element at index 2: {arr[2]}")
print(f"Element at index 4: {arr[4]}")

# Modifying elements
arr[1] = 25
print(f"After modifying index 1: {arr}")

# Array length
print(f"Array length: {len(arr)}")

# Adding elements
arr.append(60)  # Add to end
print(f"After appending 60: {arr}")

arr.insert(2, 35)  # Insert at specific index
print(f"After inserting 35 at index 2: {arr}")

# Removing elements
removed = arr.pop()  # Remove from end
print(f"Removed {removed}, array now: {arr}")

arr.remove(25)  # Remove specific value
print(f"After removing 25: {arr}")

# =============================================================================
# 3. COMMON ARRAY PROBLEMS AND SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("3. COMMON ARRAY PROBLEMS")
print("=" * 50)

# Problem 1: Find maximum element
def find_maximum(arr):
    """Find the maximum element in an array"""
    if not arr:
        return None
    
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

# Problem 2: Find minimum element
def find_minimum(arr):
    """Find the minimum element in an array"""
    if not arr:
        return None
    
    min_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val

# Problem 3: Linear search
def linear_search(arr, target):
    """Search for an element in an array"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Return -1 if not found

# Problem 4: Reverse an array
def reverse_array(arr):
    """Reverse the elements of an array"""
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap elements
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

# Problem 5: Find sum of all elements
def array_sum(arr):
    """Calculate sum of all elements in an array"""
    total = 0
    for num in arr:
        total += num
    return total

# Problem 6: Count occurrences of an element
def count_occurrences(arr, target):
    """Count how many times an element appears in an array"""
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

# Testing the functions
test_arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print(f"Test array: {test_arr}")
print(f"Maximum element: {find_maximum(test_arr)}")
print(f"Minimum element: {find_minimum(test_arr)}")
print(f"Sum of elements: {array_sum(test_arr)}")
print(f"Index of 8: {linear_search(test_arr, 8)}")
print(f"Index of 10: {linear_search(test_arr, 10)}")
print(f"Count of 3: {count_occurrences(test_arr, 3)}")

# Test reverse
arr_copy = test_arr.copy()
print(f"Original: {arr_copy}")
print(f"Reversed: {reverse_array(arr_copy)}")

# =============================================================================
# 4. TWO POINTER TECHNIQUE
# =============================================================================

print("\n" + "=" * 50)
print("4. TWO POINTER TECHNIQUE")
print("=" * 50)

# Problem: Remove duplicates from sorted array
def remove_duplicates_sorted(arr):
    """Remove duplicates from a sorted array using two pointers"""
    if not arr:
        return []
    
    write_index = 1
    for read_index in range(1, len(arr)):
        if arr[read_index] != arr[read_index - 1]:
            arr[write_index] = arr[read_index]
            write_index += 1
    
    return arr[:write_index]

# Problem: Find pair with given sum
def find_pair_with_sum(arr, target_sum):
    """Find two numbers that add up to target sum"""
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return (arr[left], arr[right])
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    
    return None

# Testing two pointer problems
sorted_arr = [1, 1, 2, 2, 3, 4, 4, 5]
print(f"Sorted array with duplicates: {sorted_arr}")
print(f"After removing duplicates: {remove_duplicates_sorted(sorted_arr.copy())}")

sum_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Array: {sum_arr}")
print(f"Pair with sum 10: {find_pair_with_sum(sum_arr, 10)}")

# =============================================================================
# 5. SLIDING WINDOW TECHNIQUE
# =============================================================================

print("\n" + "=" * 50)
print("5. SLIDING WINDOW TECHNIQUE")
print("=" * 50)

# Problem: Find maximum sum of subarray of size k
def max_sum_subarray(arr, k):
    """Find maximum sum of subarray of size k using sliding window"""
    if len(arr) < k:
        return None
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Problem: Find longest subarray with sum <= target
def longest_subarray_with_sum(arr, target):
    """Find length of longest subarray with sum <= target"""
    left = 0
    max_length = 0
    current_sum = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Testing sliding window
window_arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
print(f"Array: {window_arr}")
print(f"Max sum of subarray of size 4: {max_sum_subarray(window_arr, 4)}")
print(f"Longest subarray with sum <= 15: {longest_subarray_with_sum(window_arr, 15)}")

# =============================================================================
# 6. TIME AND SPACE COMPLEXITY ANALYSIS
# =============================================================================

print("\n" + "=" * 50)
print("6. TIME AND SPACE COMPLEXITY")
print("=" * 50)

complexity_info = """
ARRAY OPERATION COMPLEXITIES:

Access by index: O(1) - Direct memory access
Search (linear): O(n) - Must check each element
Insert at end: O(1) - Just add to end
Insert at beginning: O(n) - Must shift all elements
Delete by index: O(n) - Must shift remaining elements
Delete by value: O(n) - Must find then shift

TWO POINTER TECHNIQUE:
Time: O(n) - Each element visited at most twice
Space: O(1) - Only using constant extra space

SLIDING WINDOW:
Time: O(n) - Each element visited at most twice
Space: O(1) - Only using constant extra space

COMMON PATTERNS:
- Brute force: O(n²) - Nested loops
- Sorting: O(n log n) - Most efficient sorting algorithms
- Hash table: O(n) - Trade space for time
"""

print(complexity_info)

# =============================================================================
# 7. PRACTICE PROBLEMS
# =============================================================================

print("\n" + "=" * 50)
print("7. PRACTICE PROBLEMS TO TRY")
print("=" * 50)

practice_problems = """
EASY LEVEL:
1. Find the largest element in an array
2. Find the second largest element
3. Check if array is sorted
4. Remove all occurrences of a number
5. Find missing number in array of 1 to n

MEDIUM LEVEL:
1. Find all pairs with given sum
2. Find majority element (appears > n/2 times)
3. Find longest increasing subsequence
4. Find maximum product subarray
5. Rotate array by k positions

HARD LEVEL:
1. Find median of two sorted arrays
2. Find kth largest element
3. Find maximum sum rectangle in 2D array
4. Find longest subarray with equal 0s and 1s
5. Find maximum profit in stock trading

TIPS FOR SOLVING:
1. Always consider edge cases (empty array, single element)
2. Think about time and space constraints
3. Start with brute force, then optimize
4. Use two pointers for sorted arrays
5. Use sliding window for subarray problems
6. Consider sorting if order doesn't matter
7. Use hash maps for frequency counting
"""

print(practice_problems)

# =============================================================================
# 8. EXAMPLE: COMPLETE SOLUTION
# =============================================================================

print("\n" + "=" * 50)
print("8. COMPLETE EXAMPLE: FIND ALL TRIPLETS WITH ZERO SUM")
print("=" * 50)

def find_triplets_with_zero_sum(arr):
    """
    Find all unique triplets that sum to zero
    Time: O(n²)
    Space: O(1) excluding output
    """
    arr.sort()  # Sort for easier handling
    triplets = []
    
    for i in range(len(arr) - 2):
        # Skip duplicates for first element
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        left = i + 1
        right = len(arr) - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == 0:
                triplets.append([arr[i], arr[left], arr[right]])
                
                # Skip duplicates
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return triplets

# Test the complete example
test_triplets = [-1, 0, 1, 2, -1, -4]
print(f"Array: {test_triplets}")
print(f"Triplets with zero sum: {find_triplets_with_zero_sum(test_triplets)}")

print("\n" + "=" * 50)
print("TUTORIAL COMPLETE! Practice these concepts regularly.")
print("=" * 50)
