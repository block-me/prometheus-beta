from itertools import combinations

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
    
    # Ensure distinct numbers
    if len(set(numbers)) != len(numbers):
        return 0
    
    # Handle edge cases
    if len(numbers) <= 1:
        return 0
    
    # Compute total sum
    total_sum = sum(numbers)
    
    # Total sum must be even to have equal subset sums
    if total_sum % 2 != 0:
        return 0
    
    # Target sum for each subset
    target_sum = total_sum // 2
    
    # Brute force for clarity and correctness
    ways = 0
    n = len(numbers)
    
    # Try all possible subset combinations
    for r in range(1, n // 2 + 1):
        for subset in combinations(numbers, r):
            # Check if this subset can form one half of the partition
            if sum(subset) == target_sum:
                complement = set(numbers) - set(subset)
                if sum(complement) == target_sum:
                    ways += 1
    
    return ways