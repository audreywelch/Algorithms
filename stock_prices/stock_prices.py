#!/usr/bin/python
import argparse

prices = [100, 90, 80, 50, 20, 10]
prices2 = [1050, 270, 1540, 3800, 2]

# O(n^2)
def find_max_profit(prices):

  # Set starting maximum profit at negative infinity
  max_profit = float("-inf")

  # Loop through n - 1 elements - all indices EXCEPT the last index
  for i in range(0, len(prices) - 1):
    current_index = i

    # Loop through each element from the current through the end of the array
    for each_price in range(current_index + 1, len(prices) - 1):
      profit = prices[each_price] - prices[current_index]

      if profit > max_profit:
        max_profit = profit
  
  return max_profit

print(find_max_profit(prices))
print(find_max_profit(prices2))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

## Nested loops are not as performant
# How can we cut out one of these loops?

## redundant work is because we keep subtracting by the same number

# we want to take our current number minus whatever the smallest number behind it is
# so even though we move on to the next index, the smallest number has not changed
# so maybe we can store not just the max_profit so far, but also for the smallest price so far
# so then we can always just subtract by smallest_price until it changes

def find_max_profit_linear(prices):
  min = prices[0]
  max = prices[0]

  # Loop through all elements in the array EXCEPT the last one
  for i in range(0, len(prices) - 1):

    # If the minimum element is bigger than the current element
    if min > prices[i]:

      # Set the current element to the minimum
      min = prices[i]

      # Set the max to the element following
      max = prices[i + 1]

    # If the maximum is less than the current element
    elif max < prices[i]:

      # Set the max to that element
      max = prices[i]
      
  return max - min

  # keep track of the smallest price we've seen so far, plus the largest profit we've gotten so far

print(find_max_profit_linear(prices))
print(find_max_profit_linear(prices2))