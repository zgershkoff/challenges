# Given a list of numbers,
# interpret it as a mountain range with someone at the highest peak
from collections import deque

# Put the string of nonnegative numbers here
data = [5, 2, 4, 2, 7, 2]

def make_mountains(data):
    """
    Prints a mountain range with a person sitting on the first highest peak.

    INPUT:
      - a list of integers
    OUTPUT:
      None (prints the mountain)
    """
    mlen = sum(data)
    # If data is empty, make empty space for the guy to sit on
    if not data:
        mlen = 2
    # If the input length is odd, account for the "half peak"
    if len(data) % 2 == 1:
        mlen += 1
    M = deque([[" " for _ in range(mlen)]])
    direction = 1 # 1 is up, -1 is down
    dir_symbols = {1: '/', -1: "\\"}
    xcoord = 0
    ycoord = 0
    xpeak = 0

    for distance in data:
        for _ in range(distance):
            M[ycoord][xcoord] = dir_symbols[direction]
            xcoord += 1
            ycoord += direction
            # record the new peak as we keep climbing
            if direction == 1 and ycoord >= len(M):
                M.append([" " for _ in range(mlen)])
                xpeak = xcoord - 1
            # if we descend below where we started,
            # add new row and adjust coordinates accordingly
            elif direction == -1 and ycoord == -1:
                M.appendleft([" " for _ in range(mlen)])
                ycoord = 0

        ycoord -= direction
        direction *= -1

    # The following draws the person and prints.
    # It's more efficient to complete the person while printing
    # Because inserting a column into a list of lists isn't easy

    # add the arms and legs
    M.append([" " for _ in range(mlen)])
    M.append([" " for _ in range(mlen)])
    M[-3][xpeak] = "<"
    M[-3][xpeak + 1] = ">"
    M[-2][xpeak] = "/"
    M[-2][xpeak + 1] = "\\"

    # add the middle section
    body_symbols = {0: "o", 1: "|"}
    i = 0
    for row in reversed(M):
        body = body_symbols.get(i, " ")
        i += 1
        print("".join(row[:xpeak+1]) + body + "".join(row[xpeak+1:]))


if __name__ == "__main__":
    make_mountains(data)
