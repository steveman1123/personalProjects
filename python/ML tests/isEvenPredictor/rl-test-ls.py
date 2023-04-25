#original code generated by chatgpt, modified
#attempt to test a pattern for if the next will be larger or smaller than the previous (similar to the larger/smaller version)

import random,json

# Define the dataset
datafile = "ds5ls.txt"
with open(datafile,'r') as f:
    data = f.readlines()
    data = [int(e) for e in data]

print(datafile)

# Initialize the Q-table
q_table = {}
for i in range(len(data)):
    q_table[i] = {'larger': 0, 'smaller': 0}

# Set the hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.1 #liklihood of making a random choice (opposed to an informed choice)

# Define the reward function
def reward(state, action):
    if action == 'larger' and data[state+1] > data[state] :
        return 1
    elif action == 'smaller' and data[state+1] < data[state] :
        return 1
    else:
        return 0

# Run the Q-learning algorithm
for i in range(10000):
    state = 0
    done = False

    while not done:
        #randomly choose an larger or smaller number 10% of the time
        if random.uniform(0, 1) < epsilon:
            action = random.choice(['larger', 'smaller'])
        else:
            #get the choice values of the current state
            q_values = q_table[state]
            #choose the most likely value as the action
            action = max(q_values, key=q_values.get)

        #give us the reward!
        r = reward(state, action)
        
        #move on to the next state
        next_state = state + 1
        
        
        if next_state == len(data) - 1:
            done = True
            q_table[state][action] += alpha * (r - q_table[state][action])
        else:
            q_next_values = q_table[next_state]
            max_q_next_value = max(q_next_values.values())
            q_table[state][action] += alpha * (r + gamma * max_q_next_value - q_table[state][action])
            state = next_state

# Use the learned Q-table to predict the next number
if q_table[len(data)-2]['larger'] > q_table[len(data)-2]['smaller']:
    print('The next number should be larger')
else:
    print('The next number should be smaller')


'''
In this example, we first define the dataset as a list of integers. We then initialize the Q-table as a dictionary, where each state-action pair has an initial Q-value of 0. We set the hyperparameters for the Q-learning algorithm, including the learning rate (alpha), discount factor (gamma), and exploration rate (epsilon). We also define a reward function that returns 1 if the predicted action is correct and 0 otherwise.

We then run the Q-learning algorithm for a fixed number of iterations, where each iteration represents a complete pass through the dataset. In each iteration, we start at the beginning of the dataset (state=0) and take actions according to an epsilon-greedy policy. We update the Q-values using the Bellman equation, which incorporates the immediate reward and the estimated value of the next state-action pair. Once we reach the end of the dataset, we terminate the episode and update the Q-value for the final state-action pair.

Finally, we use the learned Q-table to predict the next number in the dataset by selecting the action with the highest Q-value for the second-to-last state in the dataset. If the predicted action is 'larger', we print 'The next number is larger'. Otherwise, we print 'The next number is smaller'.
'''





# print(json.dumps(q_table,indent=2))
predicted_smallers = [int(max(q_table[e],key=q_table[e].get)=='larger') for e in q_table]
actual_smallers = [int(data[i]>=data[i-1]) for i in range(len(data[1:]))]+[0]

print(predicted_smallers)
print(actual_smallers)

prediciton_accuracy = sum([predicted_smallers[i]==actual_smallers[i+1] for i in range(len(predicted_smallers)-1)])/(len(predicted_smallers)-1)

print("prediciton_accuracy",prediciton_accuracy)