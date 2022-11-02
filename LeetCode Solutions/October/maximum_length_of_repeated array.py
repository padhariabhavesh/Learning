# Python program to DP approach
# to above solution

# Function to find the maximum
# length of equal subarray


def FindMaxLength(A, B):
	n = len(A)
	m = len(B)

	# Auxiliary dp[][] array
	dp = [[0 for i in range(n + 1)] for i in range(m + 1)]

	# Updating the dp[][] table
	# in Bottom Up approach
	for i in range(n - 1, -1, -1):
		for j in range(m - 1, -1, -1):

			# If A[i] is equal to B[i]
			# then dp[j][i] = dp[j + 1][i + 1] + 1
			if A[i] == B[j]:
				dp[i][j] = dp[i + 1][j + 1] + 1
	maxm = 0

	# Find maximum of all the values
	# in dp[][] array to get the
	# maximum length
	for i in dp:
		for j in i:

			# Update the length
			maxm = max(maxm, j)

	# Return the maximum length
	return maxm


# Driver Code
if __name__ == '__main__':
	A = [1, 2, 8, 2, 1]
	B = [8, 2, 1, 4, 7]

	# Function call to find
	# maximum length of subarray
	print(FindMaxLength(A, B))


# work on leetcode
# class Solution:
#     def findLength(self, nums1: List[int], nums2: List[int]) -> int:
#         N,M = len(nums1),len(nums2)
#         dp = [[0 for _ in range(M+1)]for _ in range(N+1)]
#         output = 0
#         for i in range(1,N+1):
#             for j in range(1,M+1):
#                 if nums1[i-1]==nums2[j-1]:
#                     dp[i][j] = 1+dp[i-1][j-1]
#                 output = max(output,dp[i][j])
#         return output