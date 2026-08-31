def build_countdown(start):
    countdown = []
    # TODO: use a for loop with range() to count down from `start` to 1,
    # appending each number to `countdown`
    for time in range(start,0,-1):
        countdown.append(time)
    return countdown
print(build_countdown(1))