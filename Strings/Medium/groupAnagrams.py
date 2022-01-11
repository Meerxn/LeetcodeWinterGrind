class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for val in strs:
            sorted_string = "".join(sorted(val))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(val)
            else:
                anagrams[sorted_string] = [val]
        return anagrams.values()
            
        