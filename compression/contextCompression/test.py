'''
Algorithm details:
1. generate some irrational numbers or random data to some degree of accuracy/number of bits (store into file(s))
2. search these numbers for at least 9 consecutive bytes of the data to be compressed
3. create a reference to that data
4. repeat steps 2 and 3 until all data to be compressed is exhausted
5. repeat steps 2 thru 4 up to 128 times to continuously reduce size


   0  1   2   3     4  5
0x[x][XX][XX][XXXX][x][xxxX]
0: following data is compressed or not (1 bit)
1: iterations (7 bits)
2: seed index (8 bits)
3: start index (32 bits)
4: direction (0=read data forward from start index, 1=read data backwards from start index) (1 bit)
5: number of nibbles (or bytes?) to read (7 bits)

total: 8 bits (static - does not change with data size), 48 bits (variable - changes with data size)
'''

#from mpmath import mp
#import os


#set the seed/contex numbers
#should have up to 256 of these (maybe only generate if they're referenced?)
#n1 = mp.pi
#n2 = mp.phi
#n3 = mp.e
#use random data (this data is pulled from using "head -c 8000 /dev/random > ctx[x].dat"))


#convert dec to n-number bin (truncate to the lsb's, and prepend msb's if needed)
def dec2bin(d,bits=8):
  if(d>=0):
    b=("0"*(bits-len(bin(d)[2:]))+bin(d)[2:])[-bits:]
  #  b="0"*(8-len(bin(256)[2:]))+bin(257)[2:]
    return b
  else:
    raise ValueError("value must be greater than 0")

#convert a bitstream to bytes
def bits2bytes(b,bits=8):
  bytesout=b""
  if(len(b)%bits==0):
    for idx in range(0,len(b),bits):
      bytesout+=bytes(chr(int(b[idx:idx+bits],2)),"utf-8")
    return bytesout
  else:
    raise ValueError("Bitstream is not divisible by bitwidth")


#first try: convert data and dataset from bytes to bits, search full length of data  from dataset start to finish, decriment by 1 bit
#if no data found or no compression performed, or excess data in dataset, reverse dataset and try again




#stage 1: convert data and dataset to bits

#use this function to attempt to compress/encode the data
#datain is a bitstream
#iter is iteration - how many times the data has been ccompressed
iterbits=8
seedbits=3
idxbits=18
compnumbitsbits=7
uncompnumbitsbits=6

maxchunksize=75
minchunksize=41
def compress(datain,iters=0):

  print(f"datain: {len(datainb)} bits\tctx: {len(ctxb)} bits")

  #stage 2: loop through dataset looking for data

  unprocesseddata=datainb

  processeddata=dec2bin(iters,iterbits)

  while len(unprocesseddata)>0:
    print("unprocessed:",len(unprocesseddata))
    for d in range(maxchunksize,minchunksize,-1):
      chunksize=min(len(unprocesseddata),d-1)
      if(len(unprocesseddata)>0):
        for c in range(len(ctxb)-d):
          if(datainb[:chunksize]==ctxb[c:c+chunksize]):
            print(f"processed chunk length {chunksize}")
            chunkiscompressed="1"
            seed=dec2bin(ctxnum,seedbits)
            isreversed="0" #TODO: incorporste reversing of chunk or dataset
            startidx=dec2bin(c,idxbits)
            numbits=dec2bin(chunksize,compnumbitsbits) #could be made smaller if we just add the minchunksize (assuming a set minchunksize) then make this as big as the range og chunk sizes (len(bin(maxchunksize-minchunksize)), then hard code to interpret it as adding the minchunk size)

            processedchunk=chunkiscompressed+seed+isreversed+startidx+numbits
            unprocesseddata=unprocesseddata[chunksize:]
            break
          elif(chunksize<=minchunksize):
            #TODO: if it ever gets too small, loop through seeds until either seeds are exhausted or it can be compressed
            print(f"chunk is too small to compress (length: {chunksize})")
            chunkiscompressed="0"
            numbits=dec2bin(chunksize,uncompnumbitsbits)
            processedchunk=chunkiscompressed+numbits+datainb[:chunksize]
            unprocesseddata=unprocesseddata[chunksize:]
            break

    processeddata+=processedchunk
    print("processed:",len(processeddata),"\n\n")
  return processeddata




#stage 3: attempt to decode/decompress data for validation

#use this function to decompress data
#datain is a bitstream
def decompress(datain):
  decompdata=""
  iter=255
  while iter>=0:
    iter=int(datain[:8],2) #first byte contains the iteration number
    unprocesseddata=datain[8:]

    print("iteration",iter,"input",unprocesseddata)
    
    while len(unprocesseddata)>0:
      iscompressed=int(unprocesseddata[0])
      if(iscompressed):
        print("chunk is compressed")
        seed=int(unprocesseddata[1:1+seedbits],2)
        isreversed=unprocesseddata[1+seedbits]
        startidx=int(unprocesseddata[1+seedbits:1+seedbits+idxbits],2)
        numbits=int(unprocesseddata[1+seedbits+idxbits:1+seedbits+idxbits+compnumbitsbits],2)
        
        print("seed",seed,"reversed",isreversed,"startidx",startidx,"numbits",numbits)
        
        with open(f"{ctxdir}ctx{seed}.dat",'rb') as f:
          ctx = f.read()
          f.close()

        ctxb = "".join([dec2bin(e) for e in ctx])
        
        decompchunk=ctxb[startidx:startidx+numbits]
        decompdata+=decompchunk

        unprocesseddata=unprocesseddata[1+seedbits+idxbits+compnumbitsbits:]

      else:
        print("chunk is not compressed")
        numbits=int(unprocesseddata[1:uncompnumbitsbits+1],2)
        print("numbits",numbits)
        decompchunk=unprocesseddata[1+uncompnumbitsbits:uncompnumbitsbits+numbits+1]
        decompdata+=decompchunk

        unprocesseddata=unprocesseddata[1+uncompnumbitsbits+numbits:]
        
    print("output",len(decompdata))
    if(iter==0): break
    
  return decompdata




ctxnum=1
ctxdir="./contextFiles/"
ctxfile=f"./contextFiles/ctx{ctxnum}.dat"

with open(ctxfile,'rb') as f:
  ctx = f.read()
  f.close()

datain = b"Hello, World. This is a test."

datainb = "".join([dec2bin(e) for e in datain])
ctxb = "".join([dec2bin(e) for e in ctx])



dataout = compress(datainb)

print("unprocessed data",datainb)
print("processed data",dataout)
print("\n\n")

verifydata = decompress(dataout)
verification = bits2bytes(verifydata)

print(verification)
