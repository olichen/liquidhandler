from opentrons import protocol_api

metadata = {
    'protocolName': 'OT Transfer',
    'author': 'Oliver Chen <olichen@ucdavis.edu>',
    'apiLevel': '2.2'
}


def run(protocol: protocol_api.ProtocolContext):
    tip_racks = []
    tip_rack = protocol.load_labware('geb_96_tiprack_10ul', 1)
    tip_racks.append(tip_rack)
    pipette = protocol.load_instrument('p10_single', mount='right', tip_racks=tip_racks)

    src_plate = protocol.load_labware('appliedbiosystems_96_wellplate_100ul', 1)
    dest_plate = protocol.load_labware('appliedbiosystems_96_wellplate_100ul', 1)
    pipette.transfer(12, src_plate['A1'], dest_plate['A1'])
    pipette.transfer(22, src_plate['B1'], dest_plate['B1'])
    pipette.transfer(12, src_plate['C1'], dest_plate['C1'])
    pipette.transfer(43, src_plate['D1'], dest_plate['D1'])
    pipette.transfer(32, src_plate['E1'], dest_plate['E1'])
    pipette.transfer(23, src_plate['F1'], dest_plate['F1'])
    pipette.transfer(45, src_plate['G1'], dest_plate['G1'])
    pipette.transfer(12, src_plate['H1'], dest_plate['H1'])
    pipette.transfer(22, src_plate['A2'], dest_plate['A2'])
    pipette.transfer(12, src_plate['B2'], dest_plate['B2'])
    pipette.transfer(43, src_plate['C2'], dest_plate['C2'])
    pipette.transfer(32, src_plate['D2'], dest_plate['D2'])
    pipette.transfer(23, src_plate['E2'], dest_plate['E2'])
    pipette.transfer(12, src_plate['F2'], dest_plate['F2'])
    pipette.transfer(22, src_plate['G2'], dest_plate['G2'])
    pipette.transfer(12, src_plate['H2'], dest_plate['H2'])
    pipette.transfer(43, src_plate['A3'], dest_plate['A3'])
    pipette.transfer(32, src_plate['B3'], dest_plate['B3'])
    pipette.transfer(23, src_plate['C3'], dest_plate['C3'])
    pipette.transfer(45, src_plate['D3'], dest_plate['D3'])
    pipette.transfer(12, src_plate['E3'], dest_plate['E3'])
    pipette.transfer(22, src_plate['F3'], dest_plate['F3'])
    pipette.transfer(12, src_plate['G3'], dest_plate['G3'])
    pipette.transfer(43, src_plate['H3'], dest_plate['H3'])
    pipette.transfer(32, src_plate['A4'], dest_plate['A4'])
    pipette.transfer(23, src_plate['B4'], dest_plate['B4'])
    pipette.transfer(45, src_plate['C4'], dest_plate['C4'])
    pipette.transfer(12, src_plate['D4'], dest_plate['D4'])
    pipette.transfer(22, src_plate['E4'], dest_plate['E4'])
    pipette.transfer(12, src_plate['F4'], dest_plate['F4'])
    pipette.transfer(43, src_plate['G4'], dest_plate['G4'])
    pipette.transfer(32, src_plate['H4'], dest_plate['H4'])
    pipette.transfer(23, src_plate['A5'], dest_plate['A5'])
    pipette.transfer(45, src_plate['B5'], dest_plate['B5'])
    pipette.transfer(12, src_plate['C5'], dest_plate['C5'])
    pipette.transfer(22, src_plate['D5'], dest_plate['D5'])
    pipette.transfer(12, src_plate['E5'], dest_plate['E5'])
    pipette.transfer(43, src_plate['F5'], dest_plate['F5'])
    pipette.transfer(32, src_plate['G5'], dest_plate['G5'])
    pipette.transfer(23, src_plate['H5'], dest_plate['H5'])
    pipette.transfer(12, src_plate['A6'], dest_plate['A6'])
    pipette.transfer(22, src_plate['B6'], dest_plate['B6'])
    pipette.transfer(12, src_plate['C6'], dest_plate['C6'])
    pipette.transfer(43, src_plate['D6'], dest_plate['D6'])
    pipette.transfer(32, src_plate['E6'], dest_plate['E6'])
    pipette.transfer(23, src_plate['F6'], dest_plate['F6'])
    pipette.transfer(45, src_plate['G6'], dest_plate['G6'])
    pipette.transfer(12, src_plate['H6'], dest_plate['H6'])
    pipette.transfer(22, src_plate['A7'], dest_plate['A7'])
    pipette.transfer(12, src_plate['B7'], dest_plate['B7'])
    pipette.transfer(12, src_plate['C7'], dest_plate['C7'])
    pipette.transfer(22, src_plate['D7'], dest_plate['D7'])
    pipette.transfer(12, src_plate['E7'], dest_plate['E7'])
    pipette.transfer(43, src_plate['F7'], dest_plate['F7'])
    pipette.transfer(32, src_plate['G7'], dest_plate['G7'])
    pipette.transfer(23, src_plate['H7'], dest_plate['H7'])
    pipette.transfer(45, src_plate['A8'], dest_plate['A8'])
    pipette.transfer(12, src_plate['B8'], dest_plate['B8'])
    pipette.transfer(22, src_plate['C8'], dest_plate['C8'])
    pipette.transfer(12, src_plate['D8'], dest_plate['D8'])
    pipette.transfer(43, src_plate['E8'], dest_plate['E8'])
    pipette.transfer(32, src_plate['F8'], dest_plate['F8'])
    pipette.transfer(23, src_plate['G8'], dest_plate['G8'])
    pipette.transfer(12, src_plate['H8'], dest_plate['H8'])
    pipette.transfer(22, src_plate['A9'], dest_plate['A9'])
    pipette.transfer(12, src_plate['B9'], dest_plate['B9'])
    pipette.transfer(43, src_plate['C9'], dest_plate['C9'])
    pipette.transfer(32, src_plate['D9'], dest_plate['D9'])
    pipette.transfer(23, src_plate['E9'], dest_plate['E9'])
    pipette.transfer(45, src_plate['F9'], dest_plate['F9'])
    pipette.transfer(12, src_plate['G9'], dest_plate['G9'])
    pipette.transfer(12, src_plate['H9'], dest_plate['H9'])
    pipette.transfer(22, src_plate['A10'], dest_plate['A10'])
    pipette.transfer(12, src_plate['B10'], dest_plate['B10'])
    pipette.transfer(43, src_plate['C10'], dest_plate['C10'])
    pipette.transfer(32, src_plate['D10'], dest_plate['D10'])
    pipette.transfer(23, src_plate['E10'], dest_plate['E10'])
    pipette.transfer(45, src_plate['F10'], dest_plate['F10'])
    pipette.transfer(12, src_plate['G10'], dest_plate['G10'])
    pipette.transfer(22, src_plate['H10'], dest_plate['H10'])
    pipette.transfer(12, src_plate['A11'], dest_plate['A11'])
    pipette.transfer(43, src_plate['B11'], dest_plate['B11'])
    pipette.transfer(32, src_plate['C11'], dest_plate['C11'])
    pipette.transfer(23, src_plate['D11'], dest_plate['D11'])
    pipette.transfer(12, src_plate['E11'], dest_plate['E11'])
    pipette.transfer(22, src_plate['F11'], dest_plate['F11'])
    pipette.transfer(12, src_plate['G11'], dest_plate['G11'])
    pipette.transfer(43, src_plate['H11'], dest_plate['H11'])
    pipette.transfer(32, src_plate['A12'], dest_plate['A12'])
    pipette.transfer(23, src_plate['B12'], dest_plate['B12'])
    pipette.transfer(45, src_plate['C12'], dest_plate['C12'])
    pipette.transfer(12, src_plate['D12'], dest_plate['D12'])
    pipette.transfer(22, src_plate['E12'], dest_plate['E12'])
    pipette.transfer(12, src_plate['F12'], dest_plate['F12'])
    pipette.transfer(43, src_plate['G12'], dest_plate['G12'])
    pipette.transfer(32, src_plate['H12'], dest_plate['H12'])
