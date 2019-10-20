
import numpy as np

class SysState(object):

    def __init__(self, entries, dtype = np.float64):

        if entries is None:
            raise ValueError("Entries cannot be None")

        self._state_data = dict()

        for item in entries.keys():
            self._state_data[item] = entries[item]

        self._state_value = np.zeros(shape=(len(entries), 1), dtype=dtype)


    @property
    def states_names(self):
        return self._state_data.keys()

    @property
    def shape(self):
        return self._state_value.shape

    def add_state(self, state_name, idx):

        assert idx < self._state_value.shape[0] and idx >= 0, "Inavlid state idx"
        assert state_name not in self._state_data.keys(), "State %s already exists" % state_name
        self._state_data[state_name] = idx

    def get_n_states(self):
        return self._state_value.shape[0]

    def get_state_value_by_idx(self, idx):
        return self._state_value[idx]

    def set_state_value_by_name(self, name, value):
        idx = self._state_data[name]
        self._state_value[idx] = value

    def get_state_value_by_name(self, name):
        idx = self._state_data[name]
        return self._state_value[idx]

    def get_system_state(self):
        return self._state_data, self._state_value

    def get_system_state_value(self):
        return self._state_value

    def set_system_state_value(self, value):
        assert value.shape == self._state_value.shape, "Invalid shape. Shape %s not equal to %s" % (value.shape, self._state_value.shape)
        self._state_value = value