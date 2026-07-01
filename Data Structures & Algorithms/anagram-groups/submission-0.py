class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for entry in strs:
            key = "".join(sorted(entry))
            if key not in seen:
                seen[key] = []
            seen[key].append(entry)
        
        return list(seen.values())