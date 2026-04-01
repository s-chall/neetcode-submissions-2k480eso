class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashT = {}
        for i in nums:
            if i not in hashT:
                hashT[i] = 0
            hashT[i] += 1

        arr = sorted(hashT.items(), key=lambda x: -x[1])
        return [x[0] for x in arr[:k]]