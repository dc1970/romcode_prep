import os
import sys
filename = 'tip_rom.bin'
outfile0 = 'TIP_ROM_HI_TAY0_verilog.rcf '
outfile1 = 'TIP_ROM_LO_TAY0_verilog.rcf'

hexLines = os.popen('convert_bin2hex ' + sys.argv[1]).read().splitlines()


rom_size_in_dwords: int = 16384
low_rom = open(outfile0, 'w')
high_rom = open(outfile1, 'w')
binLines = []
for line in hexLines:
    binLines.append(bin(int(line, 16))[2:].zfill(32))

mem_index = 0
current_rom = low_rom
print("Starting " + outfile0)
for i in range(0, len(binLines)):
    if i == rom_size_in_dwords and current_rom == low_rom:
        current_rom = high_rom
        print('Wrote: {} lines to {}'.format(str(mem_index), outfile0))
        print("Starting " + outfile1)
        mem_index = 0
    current_rom.write(binLines[i] + '\n')
    mem_index += 1
print('Wrote: {} lines to {}'.format(str(mem_index), outfile1))
