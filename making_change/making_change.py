#!/usr/bin/python

import sys

def making_change(amount, denominations):
  
  # base cases
  # if amount is zero
  if amount == 0:
    return 1

  # if amount is negative
  if amount < 0:
    return 0

  # Don't have any denominations & we still have money we are supposed to be making change for - we are out of money to make change with
  if len(denominations) == 0 and amount > 0:
    return 0
  else:
    # get last element from denominations list and subtract that from amount
    # whatever the denomination was that we got out of the end of the array, we are subtracting that from the amount because we are using that coin to count towards the amount
    return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])

making_change(10, [1, 2, 5])

# becomes: m_c(10 - 5, [1, 2, 5]) + m_c(10, [1, 2])
m_c(o, [1, 2, 5]) + m_c(10, [1, 2]) + m_c(8, [1, 2]) + m_c(10, [1])
## -> m_c(5 - 5, [1, 2, 5]) + m_c(5, [1])
### -> first one returns 1 (b/c less than zero)
  


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")