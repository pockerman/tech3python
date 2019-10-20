"""
Representation of a differential drive
"""

from .vehicle_base import VehicleBase
from systems.system_state import SysState


class DiffDriveVehicleState(SysState):

    def __init__(self):
        SysState.__init__(n_entries=3)
        self.add_state(state_name="x", idx=0)
        self.add_state(state_name="y", idx=1)
        self.add_state(state_name="theta", idx=2)



class DiffDriveVehicle(VehicleBase):

    """
    DiffDriveVehicle models a differential drive system
    """

    def __init__(self,  properties=None, state=DiffDriveVehicleState()):
        VehicleBase.__init__(self, state=state, properties=properties)
        self._state = None


        self._propulsion = None

  
