The Dominant Signal
Given a list of items, return every item that appears at the maximum frequency. If multiple items are tied at the top, include all of them. Sort the result ascending.

def most_frequent(items: list) -> list:
  count = {}
  max_freq = 0
  for n in items:
    count[n] = count.get(n, 0) + 1
    max_freq = max(max_freq, count[n])
    
  result = []
  for key, value in count.items():
    if value == max_freq:
      result.append(key)
    
  return result

#####################################################





