from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # res = []
        # for i in (Counter(nums)).items():
        #     if (i[1])>=k:res.append(i[0])
        # return sorted(Counter(nums), key=lambda x: x[1],reverse=True)[:k]
        a = list(Counter(nums).most_common(k))
        return [i[0] for i in a]

        