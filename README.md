# romcode_prep
ROM code preparation scripts

All scrip get the <file name>.bin as a parameter 

Scripts description
* prep_tip_rom.py: Convert .bin to two HEX files
* prep_tip_bin2bin.py: Convert .bin to two binary files
* convert_bin2bin.py: Convert bin to 1 binary file

bin2bin_and_split_and_parity_and_padding
 * Based on Arik script
 * Take TIP rom image (bin file)
 * Convert to binary rcf file
 * Add 4 bits parity
 * Split to two images
