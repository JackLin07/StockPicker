def ArrayChallenge(arr):
  # we use two pointers to track. Left is best day to 
  # buy and right is best day to sell
  left = 0
  right = 1
  # case where there is no profitable selling point, we return -1
  max_profit = -1
  # a while loop to go through the entire array
  while right < len(arr):
    # initialise the current profit for the instance
    currentProfit = arr[right] - arr[left]
    # compare if price on right is higher than left
    if arr[left] < arr[right]:
      # if so we want to compare the current max_profit to the previous one
      max_profit = max(currentProfit, max_profit)
    else:
      # the current price is still higher, we shift the current price to the 
      # new right for next instance
      left = right
    # go next
    right += 1
  return max_profit

# driver
if __name__ == "__main__"":
  print(ArrayChallenge(input()))
