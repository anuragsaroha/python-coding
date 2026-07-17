"""
You are managing a product development team, and the latest release has failed quality checks.
Because each version is built on top of the previous one, once a version is bad, every version after it is also bad.

You are given an array of n versions [1,2,…,n], and your task is to determine the first version in this sequence that is bad—the version that causes all later versions to be bad as well.

You have access to an API isBadVersion(version) that returns TRUE if a given version is bad.

Your task is to find the first bad version while minimizing the number of calls to this API.

Constraints: 1 ≤ bad ≤ n ≤ 10^5
"""

from bad_version import BadVersion


class Solution(BadVersion):
    def __init__(self, bad):
        super().__init__(bad)

    def first_bad_version(self, n):
        # initial search space is [1, n]
        l, r = 1, n + 1

        while l < r:
            mid = (l + r) // 2
            if self.is_bad_version(mid):
                # mid is bad, so the first bad version is in [l, mid]
                r = mid
            else:
                # mid is good, so the first bad version is in [mid+1, r]
                l = mid + 1

        # return -1 if no bad version is found, otherwise return the first bad version
        return r if r != n + 1 else -1


# Test cases
def main():
    versions = [6, 8, 9, 11, 8]
    bad_versions = [3, 5, 1, 11, 4]

    for i in range(len(versions)):
        solution = Solution(bad_versions[i])
        print(i + 1, ".\tNumber of versions: ", versions[i], sep="")
        first_bad = solution.first_bad_version(versions[i])
        print("\n\tFirst bad version: ", first_bad)
        if first_bad == bad_versions[i]:
            print("\tTest case passed!")
        else:
            print("\tTest case failed!")
        print("-" * 100)


if __name__ == "__main__":
    main()
