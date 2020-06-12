class ProtocolFormatter:
    def getHeader(self):
        return (
            "from opentrons import protocol_api\n"
            "\n"
            "metadata = {\n"
            "    'protocolName': 'OT Transfer',\n"
            "    'author': 'Oliver Chen <olichen@ucdavis.edu>',\n"
            "    'apiLevel': '2.2'\n"
            "}\n\n"
            "def run(protocol: protocol_api.ProtocolContext):\n"
            )

    def getTipRack(self, rack_type, rack_location):
        return self.getLabware('tip_rack', rack_type, rack_location)

    def getSrcPlate(self, plate_type, plate_location):
        return self.getLabware('src_plate', plate_type, plate_location)

    def getDestPlate(self, plate_type, plate_location):
        return self.getLabware('dest_plate', plate_type, plate_location)

    def getLabware(self, labware_name, labware_type, labware_location):
        return "    {0} = protocol.load_labware('{1}', {2})\n" \
            .format(labware_name, labware_type, labware_location)

    def getPipette(self, pipette_type, pipette_location):
        return "    pipette = protocol.load_instrument(" \
            "'{0}', mount = '{1}', tip_racks = [{2}])\n\n" \
            .format(pipette_type, pipette_location, 'tip_rack')

    def getSingleTransfer(self, volume, well):
        return "    pipette.transfer(" \
            "{0}, src_plate['{1}'], dest_plate['{1}'])\n" \
            .format(volume, well)

    def getMultiTransfer(self, volume, column):
        return "    pipette.transfer({0}, " \
            "src_plate.columns_by_name()['{1}'], " \
            "dest_plate.columns_by_name()['{1}'])\n" \
            .format(volume, column)