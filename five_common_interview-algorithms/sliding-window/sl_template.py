""" 
Given an array,
Return the maximum or minimum subrange that satisfies a given condition

Two pointers (left and right)
expanding window
contracting window (find optimal range or stop condition)

A sliding window approach generally helps us reduce the time complexity for brute force approaches

"""

# Sliding Window Pseudocode 

# def sliding_window(nums):
    # Iterate over elements in our input
        # Expand the window
        # Meet the condition to stop expansion
            # Process the current window   
            # Contract the window