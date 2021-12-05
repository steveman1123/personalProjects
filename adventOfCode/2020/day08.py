import copy

with open('day08in.txt','r') as f:
  t = f.read().replace('+','').split('\n') #remove '+' right away and split into individual commands

boot = [[e[:3],int(e[4:]),0] for e in t] #split command and number into different cells, and add a hasRun element


#acc==0 for the first run, it should stop if acc>0 and loc has returned to the first loc

def runBoot(c):
  c = copy.deepcopy(c) #make an entirely separate copy
  acc=0 #accumulator var
  loc=0 #line of code currently being run
  while(loc<len(c) and c[loc][2]==0):
    #print(loc)
    if(c[loc][0]=='acc'):
      acc += c[loc][1]
      c[loc][2] = 1
      loc += 1
    elif(c[loc][0]=='nop'):
      c[loc][2] = 1
      loc += 1
    elif(c[loc][0]=='jmp'):
      c[loc][2] = 1
      loc += c[loc][1]
  #0 means improper termination, 1 is proper
  return [acc,0] if loc<len(c) else [acc,1]

pt1 = runBoot(boot)
print pt1

pt2 = [0,0]
op2rep = 0 #the nth line to change
#while the boot stops via infinite loop
while(not pt2[1]):
  c2 = copy.deepcopy(boot) #make an entirely separate copy of the boot sequence
  if(c2[op2rep][0]=='jmp'): #swap the functions
    c2[op2rep][0]='nop'
  elif(c2[op2rep][0]=='nop'):
    c2[op2rep][0]='jmp'
  
  if(c2[op2rep][0]!='acc'): #only run the boot if we changed something (i.e. if it was a acc, then we didn't change anything (makes it run faster))
    pt2 = runBoot(c2)
  op2rep += 1 #add to the index of the operation

print pt2
