"""
The matrix represents a complete weighted graph, where weights can be negative.
Dijkstra does not work with negative values, but other algorithms, such as Floyd do.
So we apply Floyd to find the shortest path between 1, 2, ... N different bunnies and keep the best one.
"""

import itertools

def path_from_permutation(perm):
  perm = list(perm)
  perm = [0] + perm + [-1]
  path = list()
  for i in range(1, len(perm)):
    path.append((perm[i - 1], perm[i]))
  return path

def prepare_floyd(time_table):
  n = len(time_table)
  
  for i in range(n):
    for j in range(n):
      for k in range(n):
        if time_table[j][k] > time_table[j][i] + time_table[i][k]:
          time_table[j][k] = time_table[j][i] + time_table[i][k]
  return time_table

def solution(time_table, time_limit):
  rows = len(time_table)
  n_of_bunnies = rows - 2
  time_table = prepare_floyd(time_table)        

  for r in range(rows):
    if time_table[r][r] < 0:
      return [i for i in range(n_of_bunnies)]

  for i in reversed(range(n_of_bunnies + 1)):
    for permutation in itertools.permutations(range(1, n_of_bunnies + 1), i):
      total_time = 0
      path = path_from_permutation(permutation)
      for start, end in path:
        total_time += time_table[start][end]
      if total_time <= time_limit:
        return sorted(list(i-1 for i in permutation))
  return None