# Read input file
with open('input.txt', 'r') as f:
  rotations = f.read().strip().split('\n')

# Start at position 50
position = 50
zero_count = 0

# Process each rotation
for rotation in rotations:
  direction = rotation[0]
  distance = int(rotation[1:])

  if direction == 'L':
    # Left means toward lower numbers
    position = (position - distance) % 100
  else:  # direction == 'R'
    # Right means toward higher numbers
    position = (position + distance) % 100

  # Check if dial points at 0 after any rotation
  if position == 0:
    zero_count += 1

# Solve and print the answer
password = zero_count
print(f"The password is: {password}")