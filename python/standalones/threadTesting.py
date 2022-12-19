#this file tests how threading works when changing a global variable

import threading, time



def main():
  global test
  
  while True:
    if('test' not in [t.getName() for t in threading.enumerate()]):
      testThread = threading.Thread(target=testThreadFxn)
      testThread.setName('test')
      testThread.start()
    print(f"main {test}")
    time.sleep(5)
    test.discard(list(test)[0])

def testThreadFxn():
  global test
  while True:
    test.add(len(test))
    test.add(len(test))
    print(f"thread {test}")
    time.sleep(1)
    rmEle()
  

def rmEle():
  global test
  test.discard(list(test)[0])


if __name__ == '__main__':
  global test
  
  test = set()
  
  main()