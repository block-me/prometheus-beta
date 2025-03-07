def tim_sort(arr):
    """
    Implement Tim sort algorithm for sorting a list.
    
    Tim sort is a hybrid sorting algorithm that combines merge sort and insertion sort,
    designed to perform well on many kinds of real-world data.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list or contains unsortable elements
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Define constants for Tim sort
    MIN_MERGE = 32
    
    def insertion_sort(arr, left, right):
        """
        Perform insertion sort on a subarray
        
        Args:
            arr (list): The list to be partially sorted
            left (int): Starting index of the subarray
            right (int): Ending index of the subarray
        """
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    
    def merge(arr, left, mid, right):
        """
        Merge two sorted subarrays
        
        Args:
            arr (list): The list containing subarrays to merge
            left (int): Starting index of the first subarray
            mid (int): Ending index of the first subarray
            right (int): Ending index of the second subarray
        """
        # Calculate lengths of two subarrays to be merged
        len1 = mid - left + 1
        len2 = right - mid
        
        # Create temporary arrays
        left_arr = arr[left:mid+1]
        right_arr = arr[mid+1:right+1]
        
        # Merge the temporary arrays
        i = j = 0
        k = left
        
        while i < len1 and j < len2:
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # Copy remaining elements of left_arr if any
        while i < len1:
            arr[k] = left_arr[i]
            k += 1
            i += 1
        
        # Copy remaining elements of right_arr if any
        while j < len2:
            arr[k] = right_arr[j]
            k += 1
            j += 1
    
    def tim_sort_internal(arr, n):
        """
        Internal implementation of Tim sort
        
        Args:
            arr (list): The list to be sorted
            n (int): Length of the list
        """
        # Sort individual subarrays of size RUN
        for i in range(0, n, MIN_MERGE):
            insertion_sort(arr, i, min((i + MIN_MERGE - 1), (n - 1)))
        
        # Start merging from size RUN (or 32)
        size = MIN_MERGE
        while size < n:
            # Pick starting point of different subarrays of size 'size'
            for start in range(0, n, size * 2):
                # Find ending point of left subarray
                mid = start + size - 1
                end = min((start + size * 2 - 1), (n - 1))
                
                # Merge subarrays if mid is less than end
                if mid < end:
                    merge(arr, start, mid, end)
            
            # Double the size of subarrays
            size *= 2
        
        return arr
    
    # Perform Tim sort
    return tim_sort_internal(arr, len(arr))