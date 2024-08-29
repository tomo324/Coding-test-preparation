N, K = map(int, input().split())
A = list(map(int, input().split()))

poped_element = A[-K:]
A = A[:-K]

A_result = poped_element + A
print(*A_result)