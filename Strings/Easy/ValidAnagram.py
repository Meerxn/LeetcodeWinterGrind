class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for val in s:
            if val not in dict1:
                dict1[val] = 0
            else:
                dict1[val]+=1
        for val in t:
            if val not in dict2:
                dict2[val] = 0
            else:
                dict2[val]+=1
       
        return dict1 == dict2