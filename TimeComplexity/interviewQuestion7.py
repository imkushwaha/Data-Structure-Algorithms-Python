# Which of the following are equivalent to O(N)? Why

# 1. O(N + P) , where p < N/2
# 2. O(2N)
# 3. O(N + logN)
# 4. O(N + NlogN)
# 5. O(N+M)

# Answer:
# O(N + P) = O(N)  # Keeping dominant term, drop non-dominant term
# O(2N) = O(N)     # drop constant
# O(N + logn) = O(N) # keeping dominant term, drop non-dominant term
# O(N + NlogN) = O(NlogN) # keeping dominant term, drop non-dominat term
# O(N + M) = O(N + M) , Here we don't have any establishment between M and N.

