from .helpers import format_helper
from .helpers import csv_helper


# Class that handles receiving/validating data and outputting the protocol
class ProtocolWriter:
    def __init__(self):
        self._pipette_data = None
        self._plate_data = []
        self._plate_csv = []
        self._fh = format_helper.FormatHelper()

    # Add another source of data (either pipette or plate data)
    def addData(self, data):
        if data.data_type == 'pipette':
            self._pipette_data = data
        elif data.data_type == 'plate':
            self._plate_data.append(data)

            # Add csv data. Validate multi-head transfer data
            csv_data = csv_helper.CSVReader(data.csv_file_loc)
            if self._pipette_data.isMulti():
                csv_data.validate_multi_transfer()
            self._plate_csv.append(csv_data.volumes)

    # Open the output file and write everything
    def saveOutput(self, output_file):
        with open(output_file, 'w') as f:
            f.write(self._fh.header())
            self._output_tip_racks(f)
            self._output__pipette_data(f)
            self._output_transfer_data(f)

    # Iterate through all the input data and write the tip rack definitions
    def _output_tip_racks(self, f):
        for d in self._plate_data:
            f.write(self._fh.tip_rack(d.tip_rack_name, d.tip_rack_loc))

    # Write the pipette definition
    def _output__pipette_data(self, f):
        d = self._pipette_data
        f.write(self._fh.pipette(d.pipette_name, d.pipette_loc))

    # Iterate through all the input data and write the plate definitions
    # followed by all the transfers
    def _output_transfer_data(self, f):
        for d, csv in zip(self._plate_data, self._plate_csv):
            f.write(self._fh.src_plate(d.src_plate_name, d.src_plate_loc))
            f.write(self._fh.dest_plate(d.dest_plate_name, d.dest_plate_loc))

            if self._pipette_data.isMulti():
                for i in range(0,96,8):
                    f.write(self._fh.transfer(csv[i], i))
            else:
                for i, vol in enumerate(csv):
                    f.write(self._fh.transfer(vol, i))
