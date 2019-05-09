#!/usr/bin/python

import sys

# Typically recursive functions do not exhibit good run times

def rock_paper_scissors(n):
  outcomes = []
  plays = ['rock', 'paper', 'scissors']

  def rps_helper(n, current_play):
    # base case
    # no more plays to add to this permutation
    # length of permutation list == n
    if len(current_play) == n:
      outcomes.append(current_play)
      return
    
    # keep building up our current_play, adding more possibilities
    for play in plays: # spins off multiple recursive calls
      # add this play to our current_play
      rps_helper(n, current_play + play)

  rps_helper(n, []) # we will use this list to build things up, but at the beginning it's empty

  return outcomes

rock_paper_scissors(2)

"""
# Generating Permutations

n = 2
['r, 'r'], [p, r], [s, r],
[r, p], [r, s], [,]
[,],[,],[,]

If we only had to generate the n = 2 case, we only need to generate the 2-element combinations and it simplifies the problem - double for loop

plays = [r, p, s]

for play1 in plays:
  for play2 in plays:
    [play1, play2]

    * big giveaway that we should use recursion

Recursion: Allows you to vary the number of nested loops

"""

# Iterative solution - actually has the same runtime
def rps_iterative():
  stack = []
  stack.append([])
  while len(stack) > 0:
    current_play = stack.pop() # pop off the one thing we just added 
    if n == 0 or len(current_play) == n: # equivalent to recursive base case
      output.append(current_play)
    else:
      for play in plays:
        stack.append(current_play + play)
  return output


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')