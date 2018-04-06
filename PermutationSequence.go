// Given n and k, return the kth permutation sequence. n decides the length of a list in order of [1,2,3,…,n].
// Note: This implementation is not the most efficient due to a loop which deletes a single element from the array by creating a new array. 

func getPermutation(n int, k int) string {
    
    solution := ""
    nums := make([]int, n)
        
    for i := 0; i < n; i++ {
        nums[i] = i+1
	}
    
    factorial := make([]int, n+1)
    factorial[0] = 1
    
     for i := 1; i <= n; i++ {
         factorial[i] = factorial[i-1] * i
	}
    

    for i := 1; i <= n; i++{
        newNumIndex := (k-1)/factorial[n-i]
        solution += strconv.Itoa(nums[newNumIndex])
        nums = append(nums[:newNumIndex], nums[newNumIndex+1:]...)
        k -= newNumIndex*factorial[n-i]
    }
    
    return solution
    
}
