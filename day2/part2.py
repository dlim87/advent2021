depth = 0
position = 0
aim = 0
f = open("day2.txt", "r")
lines = f.readlines()
for line in lines:
  direction, value = line.split(" ")
  value = int(value)
  if direction == 'forward':
    position += value
    depth += aim * value
  elif direction == 'up':
    aim -= value
  elif direction == 'down':
    aim += value
  depth = 0 if depth < 0 else depth
  print(f'{direction}-{value}: depth {depth} position {position}')
print(depth*position)