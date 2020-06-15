from context import ot2_protocol_generator
from ot2_protocol_generator import protocol_data
from ot2_protocol_generator import config

import unittest


class TestProtocolData(unittest.TestCase):
    def setUp(self):
        self.data = protocol_data.ProtocolData(
                tip_rack_name=config.TIP_RACK_NAMES[0],
                tip_rack_loc=config.TIP_RACK_LOCS[0],
                src_plate_name=config.PLATE_NAMES[0],
                src_plate_loc=config.PLATE_LOCS[0],
                dest_plate_name=config.PLATE_NAMES[0],
                dest_plate_loc=config.PLATE_LOCS[0],
                pipette_name=config.PIPETTE_NAMES[0],
                pipette_loc=config.PIPETTE_LOCS[0],
                pipette_type='',
                csv_file_loc='')

    def test_isValid(self):
        with self.assertRaises(ValueError):
            self.data.isValid()

        self.data.pipette_type = 'right'
        with self.assertRaises(ValueError):
            self.data.isValid()

        self.data.csv_file_loc = '/placeholder.py'
        with self.assertRaises(ValueError):
            self.data.isValid()

        self.data.src_plate_loc = config.PLATE_LOCS[1]
        self.data.dest_plate_loc = config.PLATE_LOCS[1]
        self.assertTrue(self.data.isValid())

    def test_checkMissingInput(self):
        with self.assertRaises(ValueError):
            self.data.checkMissingInput()
        #try:
        #    eight_transfer.EightTransfer(self.volumedict)
        #except Exception:
        #    self.fail('Unexpected exception')




if __name__ == '__main__':
    unittest.main()
