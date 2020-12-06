from Crypto.Util.number import long_to_bytes
import binwalk
import sys 
import os

logo = r'''
 _____                          _____   ___ _____ _____ 
|_   _|   Coded By R4GN4R      |  __ \ /   |_   _|____ |
  | | __ _ _   _ _ __ _   _ ___| |  \// /| | | |     / /
  | |/ _` | | | | '__| | | / __| | __/ /_| | | |     \ \
  | | (_| | |_| | |  | |_| \__ \ |_\ \___  | | | .___/ /
  \_/\__,_|\__,_|_|   \__,_|___/\____/   |_/ \_/ \____/  V1.0
'''
print(logo)






def brute_xor(filename):

	file2xor = open(filename, 'rb').read().hex() # target-file bytes

	bytes_len = len(file2xor)//2 # bytes length of target file

	file2xor_int = int(file2xor,16) # convert target-file bytes from hex value to dec

	for i in range(256):

		i_hex_value = hex(i)[2:].zfill(2) # brute-value
		print('XORing',filename,'with:',i_hex_value,"|",str(i)+"/255")

		xored_string = int( (bytes_len*i_hex_value).encode() ,16) # fix length of brute-value to fit to target-file's  length


		xored_file = long_to_bytes(file2xor_int^xored_string) # brute-value XOR file-string --> convert to bytes 



		xored_file = open('xored_file','wb').write(xored_file) # save xored bytes to xored_file

		for module in binwalk.scan('xored_file',signature=True,quiet=False, extract=False): # check results with binwalk 
			print('________________________________________________________________________________\n\n')

		os.remove("xored_file") 






def xor_files_list(filenames_list):

	files_values = []

	for current_file in filenames_list:
		files_values.append( int( open(current_file, 'rb').read().hex(), 16) )

	xored_files_list = files_values[0]

	for i in range(1,len(files_values)):



		xored_files_list = xored_files_list ^ files_values[i]


		

	xored_files_list = open('xored_files_list','wb').write(long_to_bytes(xored_files_list)) # save xored bytes to xored_file

	for module in binwalk.scan('xored_files_list',signature=True,quiet=False, extract=False): # check results with binwalk 
		print('________________________________________________________________________________\n\n')








if sys.argv[1] == '-b':

	if len(sys.argv[1:]) == 1:
		brute_xor(sys.argv[2])
	else:
		print("[!] Please select 1 file to brute-xor.")


elif sys.argv[1] == '-l':

	if len(sys.argv[2:]) > 1:
		xor_files_list(sys.argv[2:])

	else:
		print("[!] Please select at least 2 files to xor.")

else:
	print('============------------ Manual ------------============\n\n')
	print('Brute xor a file and check for file signatures:\npython3 bruxor.py -b <filename.xyz>\n\n' + '-'*55 + '\n')
	print('Xor many files together and check for file signatures:\npython3 bruxor.py -l <filename1.xyz> <filename2.xyz> <filename3.xyz>\n')