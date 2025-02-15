class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict = defaultdict(list)
        for w in strs:
            temp = [0]*26 ## Storage for all of the CharacterA
            for c in w:## Count each Character
                temp[ord(c)-ord('a')] +=1
            Dict[tuple(temp)].append(w)
        return list(Dict.values())
## Question Link : https://leetcode.com/problems/group-anagrams/description/
## Time Complexity : O(n * m)
## Space Complexity : O(n)