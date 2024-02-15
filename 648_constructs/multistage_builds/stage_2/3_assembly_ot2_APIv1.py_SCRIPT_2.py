from opentrons import labware, instruments, modules, robot
import numpy as np


final_assembly_dict={"A1": [["G1", "C12", "H11"], [1, 1, 1]], "B1": [["G1", "C12", "A12"], [1, 1, 1]], "C1": [["G1", "C12", "B12"], [1, 1, 1]], "D1": [["G1", "D12", "B11"], [1, 1, 1]], "E1": [["G1", "D12", "C11"], [1, 1, 1]], "F1": [["G1", "D12", "D11"], [1, 1, 1]], "G1": [["G1", "D12", "E11"], [1, 1, 1]], "H1": [["G1", "D12", "F11"], [1, 1, 1]], "A2": [["G1", "D12", "G11"], [1, 1, 1]], "B2": [["H1", "D12", "H11"], [1, 1, 1]], "C2": [["H1", "D12", "A12"], [1, 1, 1]], "D2": [["H1", "D12", "B12"], [1, 1, 1]], "E2": [["H1", "E12", "F12"], [1, 1, 1]], "F2": [["H1", "E12", "G12"], [1, 1, 1]], "G2": [["H1", "E12", "H12"], [1, 1, 1]], "H2": [["H1", "E12", "A1"], [1, 1, 2]], "A3": [["H1", "E12", "B1"], [1, 1, 2]], "B3": [["H1", "E12", "C1"], [1, 1, 2]], "C3": [["H1", "E12", "D1"], [1, 1, 2]], "D3": [["H1", "E12", "E1"], [1, 1, 2]], "E3": [["H1", "E12", "F1"], [1, 1, 2]], "F3": [["H1", "G1", "F12"], [1, 2, 1]], "G3": [["H1", "G1", "G12"], [1, 2, 1]], "H3": [["H1", "G1", "H12"], [1, 2, 1]], "A4": [["A2", "G1", "A1"], [1, 2, 2]], "B4": [["A2", "G1", "B1"], [1, 2, 2]], "C4": [["A2", "G1", "C1"], [1, 2, 2]], "D4": [["A2", "G1", "D1"], [1, 2, 2]], "E4": [["A2", "G1", "E1"], [1, 2, 2]], "F4": [["A2", "G1", "F1"], [1, 2, 2]], "G4": [["A2", "H1", "F12"], [1, 2, 1]], "H4": [["A2", "H1", "G12"], [1, 2, 1]], "A5": [["A2", "H1", "H12"], [1, 2, 1]], "B5": [["A2", "H1", "A1"], [1, 2, 2]], "C5": [["A2", "H1", "B1"], [1, 2, 2]], "D5": [["A2", "H1", "C1"], [1, 2, 2]], "E5": [["A2", "H1", "D1"], [1, 2, 2]], "F5": [["A2", "H1", "E1"], [1, 2, 2]], "G5": [["A2", "H1", "F1"], [1, 2, 2]], "H5": [["B2", "A2", "B2"], [1, 2, 2]], "A6": [["B2", "A2", "C2"], [1, 2, 2]], "B6": [["B2", "A2", "D2"], [1, 2, 2]], "C6": [["B2", "A2", "E2"], [1, 2, 2]], "D6": [["B2", "A2", "F2"], [1, 2, 2]], "E6": [["B2", "A2", "G2"], [1, 2, 2]], "F6": [["B2", "A2", "H2"], [1, 2, 2]], "G6": [["B2", "A2", "A3"], [1, 2, 2]], "H6": [["B2", "A2", "B3"], [1, 2, 2]], "A7": [["B2", "C3", "B2"], [1, 2, 2]], "B7": [["B2", "C3", "C2"], [1, 2, 2]], "C7": [["B2", "C3", "D2"], [1, 2, 2]], "D7": [["B2", "C3", "E2"], [1, 2, 2]], "E7": [["B2", "C3", "F2"], [1, 2, 2]], "F7": [["B2", "C3", "G2"], [1, 2, 2]], "G7": [["C2", "C3", "H2"], [1, 2, 2]], "H7": [["C2", "C3", "A3"], [1, 2, 2]], "A8": [["C2", "C3", "B3"], [1, 2, 2]], "B8": [["C2", "D3", "B2"], [1, 2, 2]], "C8": [["C2", "D3", "C2"], [1, 2, 2]], "D8": [["C2", "D3", "D2"], [1, 2, 2]], "E8": [["C2", "D3", "E2"], [1, 2, 2]], "F8": [["C2", "D3", "F2"], [1, 2, 2]], "G8": [["C2", "D3", "G2"], [1, 2, 2]], "H8": [["C2", "D3", "H2"], [1, 2, 2]], "A9": [["C2", "D3", "A3"], [1, 2, 2]], "B9": [["C2", "D3", "B3"], [1, 2, 2]], "C9": [["C2", "E3", "F6"], [1, 2, 1]], "D9": [["C2", "E3", "G6"], [1, 2, 1]], "E9": [["C2", "E3", "H6"], [1, 2, 1]], "F9": [["D2", "E3", "A7"], [1, 2, 1]], "G9": [["D2", "E3", "B7"], [1, 2, 1]], "H9": [["D2", "E3", "C7"], [1, 2, 1]], "A10": [["D2", "E3", "D7"], [1, 2, 1]], "B10": [["D2", "E3", "E7"], [1, 2, 1]], "C10": [["D2", "E3", "F7"], [1, 2, 1]], "D10": [["D2", "F3", "F6"], [1, 2, 1]], "E10": [["D2", "F3", "G6"], [1, 2, 1]], "F10": [["D2", "F3", "H6"], [1, 2, 1]], "G10": [["D2", "F3", "A7"], [1, 2, 1]], "H10": [["D2", "F3", "B7"], [1, 2, 1]], "A11": [["D2", "F3", "C7"], [1, 2, 1]], "B11": [["D2", "F3", "D7"], [1, 2, 1]], "C11": [["D2", "F3", "E7"], [1, 2, 1]], "D11": [["D2", "F3", "F7"], [1, 2, 1]], "E11": [["E2", "G3", "F6"], [1, 2, 1]], "F11": [["E2", "G3", "G6"], [1, 2, 1]], "G11": [["E2", "G3", "H6"], [1, 2, 1]], "H11": [["E2", "G3", "A7"], [1, 2, 1]], "A12": [["E2", "G3", "B7"], [1, 2, 1]], "B12": [["E2", "G3", "C7"], [1, 2, 1]], "C12": [["E2", "G3", "D7"], [1, 2, 1]], "D12": [["E2", "G3", "E7"], [1, 2, 1]], "E12": [["E2", "G3", "F7"], [1, 2, 1]], "F12": [["E2", "H3", "B8"], [1, 2, 1]], "G12": [["E2", "H3", "C8"], [1, 2, 1]], "H12": [["E2", "H3", "D8"], [1, 2, 1]]}
tiprack_num=4


def final_assembly(final_assembly_dict, tiprack_num, tiprack_type="tiprack-10ul"):
    """Implements final assembly reactions using an opentrons OT-2.

    Args:
    final_assembly_dict (dict): Dictionary with keys and values corresponding to destination and associated linker-ligated part wells, respectively.
    tiprack_num (int): Number of tipracks required during run.

    """

    # Constants
    CANDIDATE_TIPRACK_SLOTS = ['3', '6', '9', '2', '5', '8', '11']
    PIPETTE_MOUNT = 'right'
    MAG_PLATE_TYPE = '4ti-0960_FrameStar'
    MAG_PLATE_POSITION = '1'
    TUBE_RACK_TYPE = 'tube-rack_E1415-1500'
    TUBE_RACK_POSITION = '7'
    DESTINATION_PLATE_TYPE = 'aluminium-block_4ti-0960_FrameStar'
    TEMPDECK_SLOT = '4'
    TEMP = 20
    TOTAL_VOL = 15
    PART_VOL = 1.5
    MIX_SETTINGS = (1, 3)

    # Errors
    sample_number = len(final_assembly_dict.keys())
    if sample_number > 96:
        raise ValueError('Final assembly nummber cannot exceed 96.')

    # Tips and pipette
    slots = CANDIDATE_TIPRACK_SLOTS[:tiprack_num]
    tipracks = [labware.load(tiprack_type, slot)
                for slot in slots]
    pipette = instruments.P10_Single(mount=PIPETTE_MOUNT, tip_racks=tipracks)

    # Define Labware and set temperature
    magbead_plate = labware.load(MAG_PLATE_TYPE, MAG_PLATE_POSITION)
    tube_rack = labware.load(TUBE_RACK_TYPE, TUBE_RACK_POSITION)
    tempdeck = modules.load('tempdeck', TEMPDECK_SLOT)
    destination_plate = labware.load(
        DESTINATION_PLATE_TYPE, TEMPDECK_SLOT, share=True)
    tempdeck.set_temperature(TEMP)
    tempdeck.wait_for_temp()

    # Master mix transfers
    final_assembly_lens = []
    for values in final_assembly_dict.values():
        final_assembly_lens.append(len(values))
    unique_assemblies_lens = list(set(final_assembly_lens))
    master_mix_well_letters = ['A', 'B', 'C', 'D']
    for x in unique_assemblies_lens:
        master_mix_well = master_mix_well_letters[(x - 1) // 6] + str(x - 1)
        destination_inds = [i for i, lens in enumerate(
            final_assembly_lens) if lens == x]
        destination_wells = np.array(
            [key for key, value in list(final_assembly_dict.items())])
        destination_wells = list(destination_wells[destination_inds])
        pipette.pick_up_tip()
        pipette.transfer(TOTAL_VOL - x * PART_VOL, tube_rack.wells(master_mix_well),
                         destination_plate.wells(destination_wells),
                         new_tip='never')
        pipette.drop_tip()

    # Part transfers
    for key, values in list(final_assembly_dict.items()):
        pipette.transfer(PART_VOL, magbead_plate.wells(values),
                         destination_plate.wells(key), mix_after=MIX_SETTINGS,
                         new_tip='always')

    tempdeck.deactivate()


final_assembly(final_assembly_dict=final_assembly_dict,
               tiprack_num=tiprack_num)

for c in robot.commands():
    print(c)