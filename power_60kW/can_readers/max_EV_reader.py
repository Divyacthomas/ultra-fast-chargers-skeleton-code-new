import logging
from base_reader import BaseReader
from power_60kw.constant_manager_60kw import ConstantManager60KW
from utility import bytetobinary, binaryToDecimal

#logger = logging.getLogger(__name__)


class MaxEVvalues1(BaseReader):
    arbitration_id = 779

    def __init__(self, data):
        self.data = data
        self._global_data = ConstantManager60KW()
        self._binary_data = bytetobinary(data)

    def read_input_data(self):
        #logger.info('Reading digital input data for 60KW')
        maxev1= self._binary_data
        maxevvoltage1 = binaryToDecimal(int(maxev1[1] )+ int(maxev1[0]))
        maxevcurrent1 = binaryToDecimal(int(maxev1[3] )+ int(maxev1[2]))
        maxevpower1 =  int(maxevvoltage1 * maxevcurrent1) 
        self._global_data.set_data_maxpower_ev1(maxevpower1)

class MaxEVvalues2(BaseReader):
    arbitration_id = 1547

    def __init__(self, data):
        self.data = data
        self._global_data = ConstantManager60KW()
        self._binary_data = bytetobinary(data)

    def read_input_data(self):
        #logger.info('Reading digital input data for 60KW')
        maxev2= self._binary_data
        maxevvoltage2 = binaryToDecimal(int(maxev2[1] )+ int(maxev2[0]))
        maxevcurrent2 = binaryToDecimal(int(maxev2[3] )+ int(maxev2[2]))
        maxevpower2 =  int(maxevvoltage2 * maxevcurrent2)
        self._global_data.set_data_maxpower_ev2(maxevpower2)
