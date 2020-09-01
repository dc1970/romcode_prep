import binascii
filename = 'tip_rom.bin'
outfile0 = 'TIP_ROM_0.HEX'
outfile1 = 'TIP_ROM_1.HEX'

rom_size_in_dwords = 16384
low_rom = open(outfile0, 'w')
high_rom = open(outfile1, 'w')

with open(filename, 'rb') as f:
    content = binascii.hexlify(f.read())

content = str(content)[2:]
mem_index = 0
current_rom = low_rom
print("Starting " + outfile0)
for i in range(0, len(content),8):
    dword = content[i:i+8]
    if len(dword) < 8:
        if dword == "00'":   # Pad the last word with 00s
            dword = '00000000'
        else:   # Error if the last word is not 00
            print('Error in the ROM code last word:' + dword)
    dword_swap = dword[6:8] + dword[4:6] + dword[2:4] + dword[0:2]
    if mem_index == rom_size_in_dwords:
        current_rom = high_rom
        print('Wrote: {} lines to {}'.format(str(mem_index), outfile0))
        print("Starting " + outfile1)
        mem_index = 0
    current_rom.write(dword_swap + '\n')
    mem_index += 1
print('Wrote: {} lines to {}'.format(str(mem_index), outfile1))
