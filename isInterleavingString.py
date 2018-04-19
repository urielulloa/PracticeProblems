#Problem taken from LeetCode

#Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

#Examples:
#Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
#Output: true

#Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
#Output: false

class Solution(object):
    def isInterleave(self, s1, s2, s3): 
        #If the lengths of s1 and s2 do not add up to s3, it is impossible to inverleave them.
        if len(s3) != len(s1) + len(s2):
                return False
        self.memo = {} #Memo/Dictionary to avoid repeating recursive calls.
        return self.isInterleaveDyn(s1, s2, s3, 0, 0, 0)    
    
    # i marks the current index in s1, j marks the current index in s2, and s3 marks the current index in s3.
    def isInterleaveDyn(self, s1, s2, s3, i, j, k): 
        #If we have already solved this problem, then return the solution
        if (i, j) in self.memo:
            return self.memo[i, j]
            
        #Base Case: k == len(s3) signifies the end of the string s3.
        #k always equals i + j which means we are also at the end of strings s1 and s2.
        #This leaves us with the comparing the empty string with two other empty string which is always true.
        if k == len(s3):
            return True
            
        #Compute both cases: 
        #Case 1: Where we take the character at index i from s1 and see if it matches the current character at index k from s3
        #Case 2: Where we take the character at index j from s2 and see if it matches the current character at index k from s3
        foundSolution = False 
        if i < len(s1) and s1[i] == s3[k]:
            foundSolution = self.isInterleaveDyn(s1, s2, s3, i+1, j, k+1)
        if j < len(s2) and s2[j] == s3[k]:
            foundSolution = foundSolution or self.isInterleaveDyn(s1, s2, s3, i, j+1, k+1)
        self.memo[i, j] = foundSolution #Store the solution in our memo to avoid redudant recursive calls
            
        return foundSolution
