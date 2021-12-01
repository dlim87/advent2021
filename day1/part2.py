import queue
window = queue.Queue(3)
count = 0
current_sum = 0

with open('part1.txt') as f:
  lines = f.readlines()
  lines = [int(line.rstrip()) for line in lines]

  for line in lines:
    if not window.full():
      print(f'putting {line} into {window} sum: {current_sum}')
      current_sum += line
      window.put(line)
    else:
      leaving = window.get()
      window.put(line)
      new_sum = current_sum + line - leaving
      if new_sum > current_sum:
        print(f'{leaving} {list(window.queue)}: {current_sum} v {new_sum} increasing')
        count += 1
      else:
        print(f'{leaving} {list(window.queue)}: {current_sum} v {new_sum}')
      current_sum = new_sum
print(count)