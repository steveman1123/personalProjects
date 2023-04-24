#https://www.analyticsvidhya.com/blog/2022/03/a-hands-on-introduction-to-reinforcement-learning-with-python/
#first experiment making a reinforcement learning algo, just to understand the basics

import random

'''
terminology:
agent       - the thing trying to maximize reward
environment - the place in which the agent operates
state       - where is the agent now?
action      - the move made by the agent (trial)
reward      - the outcome of the action (either negative or positive reward) (error)
'''

#create the environment
class Environment:
  def __init__(self):
    #number of steps to try to acheive the max reward
    self.remainingSteps = 20

  #the current state of the agent. Any number of coordinates and their values can start arbitrarily
  def getObservation(self):
    return [1,2,1]

  #
  def getAction(self):
    return [-1,1]

  #
  def isDone(self):
    return self.remainingSteps==0

  #
  def action(self,int):
    if(self.isDone()):
      raise Exception("game over")
    self.remainingSteps-=1
    return random.random()
  

#create the agent
class Agent:
  def __init__(self):
    #init the reward value at 0
    self.totalRewards = 0

  #in the specified environment, the agent will perform an action
  def step(self,ob:Environment):
    #find the current state of the agent
    currObs = ob.getObservation()
    print(currObs)

    #get the actions the agent can perform
    currAction = ob.getAction()
    print(currAction)

    #perform the action and get the reward
    currReward = ob.action(random.choice(currAction))

    #add the new reward to the total
    self.totalRewards+=currReward
    print("current rewards:",self.totalRewards)


if __name__=="__main__":
  obj = Environment()
  agent = Agent()
  stepNum = 0

  while not obj.isDone():
    stepNum+=1
    print("step:",stepNum)
    agent.step(obj)

  print("total rewards:",agent.totalRewards)
