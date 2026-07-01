class Solution:

    def CreateDictionary(self, string: str):
        Stored_chars = {};
        for char in string:
            if char in Stored_chars:
                Stored_chars[char] += 1;
            else:
                Stored_chars[char] = 1;
        return Stored_chars;

    def isAnagram(self, s: str, t: str) -> bool:
        Dict_1 = self.CreateDictionary(s);
        Dict_2 = self.CreateDictionary(t);
        return Dict_1 == Dict_2