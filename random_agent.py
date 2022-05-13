from lib.CustomGemUnityWrapper import UnityToGymWrapper
from mlagents_envs.environment import UnityEnvironment
import random

NO_GRAPHICS = False
PATH_TO_BINARY = "./Build/TM-Match3.exe"


unityEnv = UnityEnvironment(PATH_TO_BINARY,no_graphics=NO_GRAPHICS)
env = UnityToGymWrapper(unityEnv)

def RandomAction(action_mask):
    actions = action_mask[0]
    actions_valid = [i for i in range(actions.size) if not actions[i]]

    selected = random.choice(actions_valid)
    return selected


state, action_mask = env.reset()


## Performing random actions as an example ##

for i in range(30):
    action = RandomAction(action_mask)
    new_state, reward, is_done, info = env.step(action)

    if is_done: #episode finished
        state, action_mask = env.reset()
    else:
        state = new_state
        action_mask = info['step'].action_mask[0]