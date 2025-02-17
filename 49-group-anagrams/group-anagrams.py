class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j)-ord('a')] +=1
            res[tuple(count)].append(i)
        return list(res.values())        