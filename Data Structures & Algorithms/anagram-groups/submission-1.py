

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[str]:
        # defaultdict(list) automatically creates an empty list [] for new keys
        res = defaultdict(list)
         
        for s in strs:
            # Sort the characters in the word and join them back to a string
            # "eat" -> ['a', 'e', 't'] -> "aet"
            sorted_s = "".join(sorted(s))
            
            # Group original word under its sorted key
            res[sorted_s].append(s)
            
        # Return all grouped lists
        return list(res.values())