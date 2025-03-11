def count_unique_paths(m: int, n: int) -> int:
    """
    Count the number of unique paths from top-left to bottom-right in an m x n grid.
    
    Only allowed movements are right or down.
    
    Args:
        m (int): Number of rows in the grid
        n (int): Number of columns in the grid
    
    Returns:
        int: Total number of unique paths to reach bottom-right corner
    
    Raises:
        ValueError: If m or n is less than 1
    """
    # Validate input
    if m < 1 or n < 1:
        raise ValueError("Grid dimensions must be positive integers")
    
    # Create a 2D dynamic programming table to store path counts
    dp = [[1] * n for _ in range(m)]
    
    # Calculate unique paths for each cell
    for i in range(1, m):
        for j in range(1, n):
            # Each cell's unique paths is sum of paths from above and left
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # Return total unique paths to bottom-right corner
    return dp[m-1][n-1]