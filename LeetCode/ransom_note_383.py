class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for i in magazine:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for j in ransomNote:
            if count.get(j) and count[j] > 0:
                count[j] -= 1
            else:
                return False

        return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)


