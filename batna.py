# BATNA Python Simple Simulation

import random

class Agent:
    def __init__(self, name, batna, utility_function):
        self.name = name
        self.batna = batna  # Minimum acceptable value for this agent
        self.utility_function = utility_function  # Function to evaluate utility of an offer

    def evaluate_offer(self, offer):
        return self.utility_function(offer)

    def is_acceptable(self, offer):
        return offer >= self.batna

class Negotiation:
    def __init__(self, agent1, agent2, total_resource):
        self.agent1 = agent1
        self.agent2 = agent2
        self.total_resource = total_resource

    def simulate(self, max_rounds=10):
        current_offer = self.total_resource / 2  # Start with an even split
        for round_num in range(1, max_rounds + 1):
            print(f"Round {round_num}: Current Offer = {current_offer:.2f}")

            # Agent 1 evaluates the offer
            if self.agent1.is_acceptable(current_offer):
                print(f"{self.agent1.name} accepts the offer of {current_offer:.2f}")
            else:
                print(f"{self.agent1.name} rejects the offer of {current_offer:.2f}")

            # Agent 2 evaluates the offer
            if self.agent2.is_acceptable(self.total_resource - current_offer):
                print(f"{self.agent2.name} accepts the offer of {self.total_resource - current_offer:.2f}")
            else:
                print(f"{self.agent2.name} rejects the offer of {self.total_resource - current_offer:.2f}")

            # If both accept, the negotiation ends
            if (
                self.agent1.is_acceptable(current_offer) and
                self.agent2.is_acceptable(self.total_resource - current_offer)
            ):
                print("\nAgreement reached!")
                print(f"{self.agent1.name} receives {current_offer:.2f}")
                print(f"{self.agent2.name} receives {self.total_resource - current_offer:.2f}")
                return

            # Modify the offer randomly for the next round (simulate counteroffers)
            adjustment = random.uniform(-1, 1) * (self.total_resource / 10)
            current_offer = max(0, min(self.total_resource, current_offer + adjustment))

        print("\nNo agreement reached after maximum rounds.")

# Define utility functions
def linear_utility(value):
    return value

# Create two agents with different BATNAs
agent1 = Agent("Agent 1", batna=40, utility_function=linear_utility)
agent2 = Agent("Agent 2", batna=50, utility_function=linear_utility)

# Define the total resource available for negotiation
total_resource = 100

# Simulate the negotiation
negotiation = Negotiation(agent1, agent2, total_resource)
negotiation.simulate()
