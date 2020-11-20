def swapbits(n):
    '''Swapp all even bits for all odd bits'''
    # mask for all even bits set to '1's -  0xAAAAAAAA
    shifteven = (n & 0xAAAAAAAA) >> 1
    # mask for all odd positions set to '1's -  0x55555555
    shiftodd = (n & 0x55555555) << 1

    # combine the bits
    result = shifteven | shiftodd

    return result
#end swapbits(n):

if __name__ == '__main__':
    n = 23

    print("Number before the swap is {0} in binary it is {1}".format(n, bin(n)))
    n = swapbits(n)
    print("Number after the swap is {0} in binary it is {1}".format(n, bin(n)))
#end if __name__ == '__main__':
