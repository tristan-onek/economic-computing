import matplotlib.pyplot as plt
import numpy as np

class MultiArmedBandit:
    def __init__(self, nArms):
        self.n_arms = nArms
        self.probabilities = np.random.rand(nArms)
        self.q_values = np.zeros(nArms)  # est. values for each arm
        self.action_counts = np.zeros(nArms)  # times that an arm was pulled

    def pull_arm(self, arm):
        """Simulates an arm being pulled, with us then getting a reward of 1 or no reward of 0."""
        return 1 if np.random.rand() < self.probabilities[arm] else 0

    def update_q_values(self, arm, reward):
        """Updates Q-value for given arm, based upon the received reward."""
        self.action_counts[arm] += 1
        self.q_values[arm] += (reward - self.q_values[arm]) / self.action_counts[arm]

    def epsilon_greedy(self, epsilon):
        """Selects an arm using the epsilon-greedy strategy."""
        if np.random.rand() < epsilon:
            return np.random.randint(self.n_arms)  # Exploration: Random arm
        else:
            return np.argmax(self.q_values)  # Exploitation: Best estimated arm

# Simulation parameters
n_arms = 5
n_iterations = 1000
epsilon = 0.1

# Initialize the multi-armed bandit
bandit = MultiArmedBandit(n_arms)

# Variables to track rewards
rewards = []
cumulative_rewards = []

total_reward = 0

for i in range(n_iterations):
    # Choose an arm using epsilon-greedy strategy
    chosen_arm = bandit.epsilon_greedy(epsilon)
    
    # Pull the chosen arm and get a reward
    reward = bandit.pull_arm(chosen_arm)
    
    # Update Q-values
    bandit.update_q_values(chosen_arm, reward)

    # Track rewards
    total_reward += reward
    rewards.append(reward)
    cumulative_rewards.append(total_reward)

# Print the results
print("Actual probabilities of each arm:", bandit.probabilities)
print("Estimated values (Q-values) of each arm:", bandit.q_values)
print("Number of times each arm was pulled:", bandit.action_counts)

# Plot the cumulative rewards
plt.figure(figsize=(10, 6))
plt.plot(cumulative_rewards, label="Cumulative Reward")
plt.xlabel("Iterations")
plt.ylabel("Cumulative Reward")
plt.title("Multi-Armed Bandit: Cumulative Reward Over Time")
plt.legend()
plt.grid()
plt.show()
