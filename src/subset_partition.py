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
    if len(numbers) <= 1:
        return 0
    
    # Compute total sum
    total_sum = sum(numbers)
    
    # Total sum must be even to have equal subset sums
    if total_sum % 2 != 0:
        return 0
    
    # Target sum for each subset
    target_sum = total_sum // 2
    
    # Memoization to avoid repeated computations
    memo = {}
    
    def count_subsets(index, current_sum):
        # Base cases
        if current_sum == target_sum:
            return 1
        if current_sum > target_sum or index >= len(numbers):
            return 0
        
        # Check memoized result
        key = (index, current_sum)
        if key in memo:
            return memo[key]
        
        # Recursive cases: include or exclude current number
        include = count_subsets(index + 1, current_sum + numbers[index])
        exclude = count_subsets(index + 1, current_sum)
        
        # Memoize and return
        memo[key] = include + exclude
        return memo[key]
    
    # Start counting subsets with a twist to count exact ways
    total_ways = count_subsets(0, 0)
    
    # Divide by 2 to account for symmetric partitions
    return max(total_ways // 2, 0)