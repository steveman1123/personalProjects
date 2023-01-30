'''
Algorithm details:
1. generate some irrational numbers or random data to some degree of accuracy/number of bits (store into file(s))
2. search these numbers for at least 9 consecutive bytes of the data to be compressed
3. create a reference to that data
4. repeat steps 2 and 3 until all data to be compressed is exhausted
5. repeat steps 2 thru 4 up to 256 times to continuously reduce size


   1   2  3      4  5
0x[XX][XX][XXXX][x][xxxX]
1: iterations (8 bits)
2: seed index (8 bits)
3: start index (32 bits)
4: direction (0=read data forward from start index, 1=read data backwards from start index) (1 bit)
5: number of nibbles (or bytes?) to read (7 bits)

total: 8 bits (static - does not change with data size), 48 bits (variable - changes with data size)
'''


datain = "Hello, World. This is a test."
print("".join([bin(ord(e))[2:] for e in datain]))