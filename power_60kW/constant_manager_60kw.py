from base_constant_manager import BaseConstantManager


class ConstantManager60KW(BaseConstantManager):
    def __init__(self, d='', pe1current=0, rc=0, vehiclestatus2=6, vehiclestatus1=6, maxev1power=0,maxev2power=0):
        super().__init__(d, pe1current, vehiclestatus2, vehiclestatus1, maxev1power,maxev2power)
        self._rc = rc

    def get_data_running_current(self):
        return self._rc

    def set_data_running_current(self, x):
        self._rc = x
