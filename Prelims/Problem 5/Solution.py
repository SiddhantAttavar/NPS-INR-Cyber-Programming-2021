# Initialize position
x = 0
y = 0

for i in range(int(input())):
    # Take input
    dir, delta = input().split()

    # Update position
    if dir == 'U':
        y += int(delta)
    elif dir == 'D':
        y -= int(delta)
    elif dir == 'L':
        x -= int(delta)
    elif dir == 'R':
        x += int(delta)

# Print the final position
print(x, y)