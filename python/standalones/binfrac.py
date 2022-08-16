#convert a decimal fraction to fractions of different bases

base = 2#int(input("base 2 thru 10: ")) #TODO: allow for different bases (and above 10)
decfrac = float(input("decimal (base 10) between 0 and 1: "))

if(decfrac>1 or decfrac<0 or base<2 or base>10):
  raise ValueError("out of bounds")

#max number of bits to include
resolution=24

binstr = "0." #output binary string
calced=0 #actual binary value
i=1
while i<resolution and calced!=decfrac:
  bit = int(decfrac>=calced+base**-i)
  binstr+=str(bit)
  calced+=bit*base**-i
  i+=1
  
  print(binstr,calced)