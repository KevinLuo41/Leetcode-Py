class Solution:

    def uniquePaths(self, m, n):
        ways = [[1] for i in range(m)]
        for i in range(1, n):
            ways[0].append(1)
        for i in range(1, m):
            for j in range(1, n):
                ways[i].append(ways[i - 1][j] + ways[i][j - 1])
        return ways[m - 1][n - 1]

    # it's pascal's triangle, we can get result by computing C(m,n), we can
    # achieve O(min(m,n))

    def uniquePaths_2(self, m, n):
        if m < n:
            return self.uniquePaths(n, m)
        if m == 1 and n == 1:
            return 1
        m, n, res = m + n - 2, n - 1, 1
        if n > (m / 2):
            n = m - n
        for i in xrange(n):
            res = res * (m - i) / (i + 1)
        return res
