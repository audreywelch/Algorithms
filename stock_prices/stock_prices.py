#!/usr/bin/python
import argparse

prices = [100, 90, 80, 50, 20, 10]

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

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))