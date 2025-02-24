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
    if len(numbers) == 0:
        return 0
    
    # Total sum must be even to have equal subset sums
    total_sum = sum(numbers)
    if total_sum % 2 != 0:
        return 0
    
    # Target sum for each subset
    target_sum = total_sum // 2
    
    # Use dynamic programming
    dp = [0] * (target_sum + 1)
    dp[0] = 1
    
    # Compute number of subsets with each sum
    for num in numbers:
        for j in range(target_sum, num - 1, -1):
            dp[j] += dp[j - num]
    
    # At this point, dp[target_sum] will contain the number of ways to make the subset
    # We divide by 2 because each partition is counted twice (A,B and B,A)
    return dp[target_sum] // 2