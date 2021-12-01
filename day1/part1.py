higher = 0
lower = 0
current = None
with open('part1.txt') as f:
  lines = f.readlines()
  lines = [int(line.rstrip()) for line in lines]
  for line in lines:
    if current == None:
      current = line
    else:
      if current > line:
        print(f'{current} {line} lower')
        lower += 1
      elif current < line:
        print(f'{current} {line} higher')
        higher += 1
      current = line
print(f'higher: {higher}, lower: {lower}')