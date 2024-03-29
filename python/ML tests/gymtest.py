#original code generated by chatGPT
#use the openai gym package to solve the CartPole problem

import gym
import numpy as np

# Define the environment
env = gym.make('CartPole-v1')

# Define the Q-learning parameters
epsilon = 0.9
discount_factor = 0.9
learning_rate = 0.8
num_episodes = 10000

# Initialize the Q-table
state_space_size = env.observation_space.shape[0]
action_space_size = env.action_space.n
q_table = np.zeros((state_space_size, action_space_size))

# Train the agent using Q-learning
for episode in range(num_episodes):
  state = env.reset()
  done = False
  while not done:
    # Choose an action using an epsilon-greedy policy
    if np.random.uniform(0, 1) < epsilon:
      action = env.action_space.sample()
    else:
      action = np.argmax(q_table[state, :])

    # Take the chosen action and observe the next state and reward
    next_state, reward, done, info = env.step(action)

    # Update the Q-table using the Bellman equation
    q_table[state, action] = (1 - learning_rate) * q_table[state, action] + learning_rate * (reward + discount_factor * np.max(q_table[next_state, :]))

    # Update the state
    state = next_state

  # Reduce the value of epsilon over time
  epsilon = epsilon * 0.99

# Test the agent
state = env.reset()
done = False
total_reward = 0
while not done:
  action = np.argmax(q_table[state, :])
  state, reward, done, info = env.step(action)
  total_reward += reward
  env.render()

print("Total reward: ", total_reward)
env.close()
