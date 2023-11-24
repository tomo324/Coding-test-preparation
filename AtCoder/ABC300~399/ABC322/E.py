from itertools import combinations

N, K, P = map(int, input().split())

ideas = []

for _ in range(N):
    idea = list(map(int, input().split()))
    ideas.append(idea)

cost = 0
for r in range(1, len(ideas) + 1):
    for comb in combinations(ideas, r):
        for i in range(len(comb)):