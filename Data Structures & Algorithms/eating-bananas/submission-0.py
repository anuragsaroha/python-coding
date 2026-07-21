class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l+r)//2
            num_hours_at_mid = self.numHoursRequiredToEatAllBananas(piles, mid)
            if num_hours_at_mid > h:
                l = mid + 1
            else:
                r = mid
        return l


    def numHoursRequiredToEatAllBananas(self, piles: List[int], rate: int) -> int:
        hours_needed = 0
        for i in range(len(piles)):
            hours_needed += math.ceil(piles[i] / rate)
        return hours_needed