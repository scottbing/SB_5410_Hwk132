SUITS = ['C', 'D', 'H', 'S']
FACE = {10: '0', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
HAND = 13


def getcard(n):
    a, b = divmod(n, HAND)
    b += 2  # adjust b
    b = b if b < 10 else FACE[b]
    #print("card = {0}{1}".format(b, SUITS[a]))

    return b, SUITS[a]


# end getcard(n):


if __name__ == '__main__':
    n = 34

    c, s = getcard(n)
    print("card = {0}{1}".format(c, s))
# end if __name__ == '__main__':
