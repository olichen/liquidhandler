from ot2_protocol_generator.helpers import config

# Formats the output code for the protocol
class FormatHelper:
    def __init__(self):
        self.cfg = config.Configuration()

    # Returns the code for the header
    def header(self):
        return ("from opentrons import protocol_api\n\n"
                "metadata = {\n"
                "    'apiLevel': '2.2'\n"
                "}\n\n\n"
                "def run(protocol: protocol_api.ProtocolContext):\n"
                "    tip_racks = []\n")

    # Returns the code to load a tip rack
    def tip_rack(self, rack_name, rack_location):
        msg = self._labware('tip_rack', rack_name, rack_location)
        msg += "    tip_racks.append(tip_rack)\n"
        return msg

    # Returns the code to load a plate
    def src_plate(self, plate_name, plate_location):
        return self._labware('src_plate', plate_name, plate_location)

    # Returns the code to load a plate
    def dest_plate(self, plate_name, plate_location):
        return self._labware('dest_plate', plate_name, plate_location)

    # Returns the code to load a piece of labware (tip rack, plate, etc)
    def _labware(self, var_name, lw_name, lw_loc):
        return (f"    {var_name} = protocol.load_labware("
                f"'{lw_name}', {lw_loc})\n")

    # Returns the code to load a pipette
    def pipette(self, p_name, p_loc):
        b_rate = self.cfg.get_transfer('BLOW_OUT_RATE')
        return ("    pipette = protocol.load_instrument("
                f"'{p_name}', mount='{p_loc}', tip_racks=tip_racks)\n"
                f"    pipette.flow_rate.blow_out = {b_rate}\n\n")

    # Returns the code to transfer volume from well to well, with blowout
    # Note that 0.2ul is added to offset the pipette inaccuracy. Perhaps this
    # should get moved to the config file.
    def transfer(self, vol, well):
        msg = "    pipette.pick_up_tip()\n"
        a_off = self.cfg.get_transfer('ASPIRATE_OFFSET')
        a_rate = self.cfg.get_transfer('ASPIRATE_RATE')
        airgap = self.cfg.get_transfer('AIR_GAP')
        d_off = self.cfg.get_transfer('DISPENSE_OFFSET')
        while vol > 0:
            xfer = min(10.0 - airgap, vol + a_off)
            msg += (f"    pipette.aspirate({xfer}, src_plate.wells()[{well}]"
                    f".bottom(), rate = {a_rate}).air_gap({airgap})\n")
            msg += (f"    pipette.dispense({xfer + airgap + d_off}, "
                    f"dest_plate.wells()[{well}])"
                    f".blow_out(dest_plate.wells()[{well}])\n")
            vol -= xfer
        msg += "    pipette.drop_tip(home_after=False)\n"
        return msg
