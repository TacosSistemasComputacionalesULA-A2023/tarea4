import os

import gym
import gym_taco_environments
import time
from agent import ValueIteration

# Allowing environment to have sounds
if "SDL_AUDIODRIVER" in os.environ:
    del os.environ["SDL_AUDIODRIVER"]

# RobotBattery-v0, FrozenLake-v1, FrozenLake-v2
env = gym.make('RobotBattery-v0', render_mode="human", delay=0.5)
agent = ValueIteration(env.observation_space.n, env.action_space.n, env.P, 0.9)

agent.solve(100)
agent.render()

observation, info = env.reset()
terminated, truncated = False, False

env.render()
time.sleep(2)

while not (terminated or truncated):
    action = agent.get_action(observation)
    observation, _, terminated, truncated, _ = env.step(action)

time.sleep(2)
env.close()