Methods for top k frequent elements  

Solution 1: sort by frequency + pick top k  
Time complexity: O(nlogn)  
Space complexity: O(n)  


Solution 2: priority queue / min heap  
Time complexity: O(nlogk)  
Space complexity: O(k)  


Solution 3: bucket sorting  
Time complexity: O(n)  
Space complexity: O(n) array -> O(k) hashtable   