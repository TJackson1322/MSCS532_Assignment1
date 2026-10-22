
# MSCS 532 - Assignment 1
# Insertion Sort in Decreasing Order

def insertion_sort_decreasing(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        # Move smaller numbers to the right
        while j >= 0 and numbers[j] < key:
            numbers[j + 1] = numbers[j]
            j -= 1

        # Put the current number in its correct position
        numbers[j + 1] = key

    return numbers


# Example numbers to sort
numbers = [12, 45, 8, 31, 20]

print("Original list:", numbers)
insertion_sort_decreasing(numbers)
print("Decreasing order:", numbers)
# Additional tests for Insertion Sort
print("\nAdditional Tests")

test_lists = [
    [5, 5, 2, 8, 2],       # Duplicate numbers
    [9, 7, 5, 3, 1],       # Already decreasing
    [-3, 10, 0, -8, 5]     # Negative numbers
]

for test in test_lists:
    print("Original:", test.copy())
    print("Sorted:", insertion_sort_decreasing(test))