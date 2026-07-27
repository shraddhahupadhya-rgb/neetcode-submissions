

class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            # Store the string length, delimiter '#', and the string itself
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string back to a list of strings.
        """
        res = []
        i = 0
        
        while i < len(s):
            # Find where the length number ends (at the '#')
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the integer length of the next string
            length = int(s[i:j])
            
            # Extract the string itself using the parsed length
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move index past the current word to process the next segment
            i = end
            
        return res

