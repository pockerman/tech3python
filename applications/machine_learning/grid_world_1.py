"""

Learn gridworld using policy evaluation
Thanks to: Gerard Martinez https://towardsdatascience.com/reinforcement-learning-rl-101-with-python-e1aa0d37d43b
Notebook: https://gist.github.com/GerardBCN/252e852c46b607c00435b830431191ad#file-policy_iterator_rl_gridworld-ipynb

"""

import numpy as np

gamma = 1  # discounting rate
reward_size = -1
grid_size = 4
termination_states = [[0, 0], [grid_size - 1, grid_size - 1]]

num_itrs = 1000


def get_action_reward(init_pos, action):
    if init_pos in termination_states:
        return init_pos, 0

    reward = reward_size
    final_pos = np.array(init_pos) + np.array(action)

    if -1 in final_pos or 4 in final_pos:
        final_pos = init_pos

    return final_pos, reward


def policy_evaluation(value_map, states, actions):
    deltas = []
    for it in range(num_itrs):

        copy_value_map = np.copy(value_map)
        delta_state = []

        for state in states:
            weighted_rewards = 0

            for action in actions:
                final_position, reward = get_action_reward(state, action)
                weighted_rewards += (1 / len(actions)) * (
                            reward + (gamma * value_map[final_position[0], final_position[1]]))

            delta_state.append(np.abs(copy_value_map[state[0], state[1]] - weighted_rewards))
            copy_value_map[state[0], state[1]] = weighted_rewards


    deltas.append(delta_state)
    value_map = copy_value_map

    if it in [0, 1, 2, 9, 99, num_itrs - 1]:
        print("Iteration {}".format(it + 1))
        print(value_map)
        print("")


def main():
    value_map = np.zeros(shape=(grid_size, grid_size))
    states = [[i, j] for i in range(grid_size) for j in range(grid_size)]
    actions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    policy_evaluation(value_map=value_map, states=states, actions=actions)


if __name__ == '__main__':
    main()
