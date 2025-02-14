class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict = defaultdict(list)
        for w in strs:
            temp = [0]*26
            for c in w:
                temp[ord(c)-ord('a')] +=1
            Dict[tuple(temp)].append(w)
        return list(Dict.values())