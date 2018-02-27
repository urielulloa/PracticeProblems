class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        if (s.length() == 0) return 0; //Base Case #1: Empty String
        if (s.length() == 1) return 1; //Base Case #2: String with a single character
        
        
        Set<Character> set = new HashSet<>(); //This set will hold all the current characters in the current substring.
        int longestSubstringLength = 0;
        int frontCharIndex = 0;
        int lastCharIndex = 0; //This represents the index of the last character in our substring

        
        while(lastCharIndex < s.length()){ 
            if (set.contains(s.charAt(lastCharIndex))){ //If we have already seen this character
                set.remove(s.charAt(frontCharIndex)); //We remove the first character in our substring
                frontCharIndex++; //Update which character if first in our substring
            }
            
            else{
                set.add(s.charAt(lastCharIndex));
                lastCharIndex++;
                longestSubstringLength = Math.max(longestSubstringLength, lastCharIndex-frontCharIndex);
            }
        }
        
        return longestSubstringLength;
    }
}