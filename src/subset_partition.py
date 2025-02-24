def count_equal_sum_partitions(numbers):
    """
    Calculate the number of ways a group of distinct numbers can be partitioned 
    into two subsets with equal sums.

    Args:
        numbers (list): A list of distinct integers.

    Returns:
        int: The number of ways to partition the numbers into two subsets with equal sums.

    Raises:
        ValueError: If the input is not a list or contains non-integer values.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list of distinct integers")
    
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    
    # Handle edge cases
    if len(numbers) == 0:
        return 0
    
    # Total sum must be even to have equal subset sums
    total_sum = sum(numbers)
    if total_sum % 2 != 0:
        return 0
    
    # Target sum for each subset
    target_sum = total_sum // 2
    
    # Dynamic programming solution using meet-in-the-middle approach
    def find_subset_counts(arr):
        # Generate all possible subset sums
        subset_sums = {0: 1}
        for num in arr:
            new_sums = subset_sums.copy()
            for curr_sum, count in subset_sums.items():
                new_sum = curr_sum + num
                new_sums[new_sum] = new_sums.get(new_sum, 0) + count
            subset_sums = new_sums
        return subset_sums
    
    # Split the list into two halves
    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]
    
    # Find subset sums for both halves
    left_sums = find_subset_counts(left_half)
    right_sums = find_subset_counts(right_half)
    
    # Count valid partitions
    total_partitions = 0
    for left_sum, left_count in left_sums.items():
        complement_sum = target_sum - left_sum
        if complement_sum in right_sums:
            total_partitions += left_count * right_sums[complement_sum]
    
    return total_partitions