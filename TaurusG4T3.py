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
  \_/\__,_|\__,_|_|   \__,_|___/\____/   |_/ \_/ \____/  V1.4
'''
print(logo)


help_string = '''
===============---------------- Manual ----------------===============\n\n
Brute-Bitwise a file and check for file signatures:
python3 TaurusG4T3.py -bx <filename.xyz> # Brute-Xor a file
python3 TaurusG4T3.py -bo <filename.xyz> # Brute-Or a file
python3 TaurusG4T3.py -ba <filename.xyz> # Brute-And a file\n\n{}\n
Bitwise many files together and check for file signatures:
python3 TaurusG4T3.py -la <filename1.xyz> <filename2.xyz> <filename3.xyz> # Brute-Xor many files together
python3 TaurusG4T3.py -lo <filename1.xyz> <filename2.xyz> <filename3.xyz> # Brute-Or many files together
python3 TaurusG4T3.py -la <filename1.xyz> <filename2.xyz> <filename3.xyz> # Brute-And many files together\n\n{}\n
Bitwise a file with a specific key:
python3 TaurusG4T3.py -kbx <filename.xyz> <key> # Xor a file with a specific key
python3 TaurusG4T3.py -kbo <filename.xyz> <key> # Or a file with a specific key
python3 TaurusG4T3.py -kba <filename.xyz> <key> # And a file with a specific key\n\n{}\n
Check if you have the last version:
python3 TaurusG4T3.py -u
\n
'''.format('-'*55,'-'*55,'-'*55)


def binwalk_scan(result_filename,save_result):

	try:
		for module in binwalk.scan(result_filename,signature=True,quiet=False, extract=False): # check results with binwalk 
			print('_'*80 + '\n\n')
	except binwalk.ModuleException as e:
		print ("Critical failure:", e)





def brute_xor(filename, key, b_op):


	if (b_op == '-bx') or (b_op == '-kbx'): bitWise_op = 'x'
	elif b_op == '-bo' or (b_op == '-kbo'): bitWise_op = 'o'
	elif b_op == '-ba' or (b_op == '-kba'): bitWise_op = 'a'
	else: print(help_string); return


	file2bitwise = open(filename, 'rb').read().hex() # target-file bytes
	bytes_len = len(file2bitwise)//2 # bytes length of target file
	file_int = int(file2bitwise,16) # convert target-file bytes from hex value to dec


	if '-k' in b_op:
		if len(key) < bytes_len:
			fixed_key = ((bytes_len//len(key)+1)*key)[:bytes_len]
		else:
			fixed_key = fixed_key[:bytes_len]

		fixed_key = fixed_key.encode().hex()
		fixed_key = int(fixed_key, 16)


		if b_op == '-kbx':
			print('XORing',filename,'with:',key)
			XORed_file = long_to_bytes(file_int ^ fixed_key)
			XORed_file = open('bitwise_temp_file','wb').write(XORed_file)

			binwalk_scan('bitwise_temp_file',None)

		elif b_op == '-kbo':
			print('ORing',filename,'with:',key)
			ORed_file = long_to_bytes(file_int | fixed_key)
			ORed_file = open('bitwise_temp_file','wb').write(ORed_file)

			binwalk_scan('bitwise_temp_file',None)

		elif b_op == '-kba':
			print('ANDing',filename,'with:',key)
			ANDed_file = long_to_bytes(file_int & fixed_key)
			ANDed_file = open('bitwise_temp_file','wb').write(ANDed_file)

			binwalk_scan('bitwise_temp_file',None)

		else:
			print(help_string)
			return

	else:


		if bitWise_op == 'x':


			for i in range(256):

				i_hex_value = hex(i)[2:].zfill(2) # brute-value
				print('XORing',filename,'with:',i_hex_value,"|",str(i)+"/255")
				XOR_string = int( (bytes_len*i_hex_value).encode() ,16) # fix length of brute-value to fit to target-file's  length
				XORed_file = long_to_bytes(file_int ^ XOR_string) # brute-value XOR file-string --> convert to bytes 
				XORed_file = open('bitwise_temp_file','wb').write(XORed_file) # save xored bytes to XORed_file

				binwalk_scan('bitwise_temp_file',None)


		elif bitWise_op == 'o':

			for i in range(256):

				i_hex_value = hex(i)[2:].zfill(2) # brute-value
				print('ORing',filename,'with:',i_hex_value,"|",str(i)+"/255")
				OR_string = int( (bytes_len*i_hex_value).encode() ,16) # fix length of brute-value to fit to target-file's  length
				ORed_file = long_to_bytes(file_int | OR_string) # brute-value XOR file-string --> convert to bytes 
				ORed_file = open('bitwise_temp_file','wb').write(ORed_file) # save xored bytes to ORed_file

				binwalk_scan('bitwise_temp_file',None)


		elif bitWise_op == 'a':

			for i in range(256):

				i_hex_value = hex(i)[2:].zfill(2) # brute-value
				print('ANDing',filename,'with:',i_hex_value,"|",str(i)+"/255")
				AND_string = int( (bytes_len*i_hex_value).encode() ,16) # fix length of brute-value to fit to target-file's  length
				ANDed_file = long_to_bytes(file_int & AND_string) # brute-value XOR file-string --> convert to bytes 
				ANDed_file = open('bitwise_temp_file','wb').write(ANDed_file) # save xored bytes to ANDed_file

				binwalk_scan('bitwise_temp_file',None)


	os.remove("bitwise_temp_file") 






def xor_files_list(filenames_list,b_op):


	if b_op == '-lx': bitWise_op = 'x'
	elif b_op == '-lo': bitWise_op = 'o'
	elif b_op == '-la': bitWise_op = 'a'
	else: print(help_string); return


	files_values = []

	for current_file in filenames_list:
		files_values.append( int( open(current_file, 'rb').read().hex(), 16) )


	if bitWise_op == 'x':
		print('XORing:',filenames_list)
		XOR_files_list = files_values[0]

		for i in range(1,len(files_values)):
			XOR_files_list = XOR_files_list ^ files_values[i] # bitwise operation

		XOR_files_list = open('XOR_files_list','wb').write(long_to_bytes(XOR_files_list)) # save xored bytes to XORed_file

		binwalk_scan('XOR_files_list',None)



	elif bitWise_op == 'o':
		print('ORing:',filenames_list)
		OR_files_list = files_values[0]

		for i in range(1,len(files_values)):
			OR_files_list = OR_files_list | files_values[i] # bitwise operation

		OR_files_list = open('OR_files_list','wb').write(long_to_bytes(OR_files_list)) # save xored bytes to XORed_file

		binwalk_scan('OR_files_list',None)



	elif bitWise_op == 'a':
		print('ANDing:',filenames_list)
		AND_files_list = files_values[0]

		for i in range(1,len(files_values)):
			AND_files_list = AND_files_list & files_values[i] # bitwise operation

		AND_files_list = open('AND_files_list','wb').write(long_to_bytes(AND_files_list)) # save xored bytes to XORed_file

		binwalk_scan('AND_files_list',None)



try:

	if '-b' in sys.argv[1]:

		if len(sys.argv[2:]) == 1:
			brute_xor(sys.argv[2], None, sys.argv[1])
		else:
			print("[!] Please select 1 file to brute-Bitwise.")


	elif '-l' in sys.argv[1]:

		if len(sys.argv[2:]) > 1:
			xor_files_list(sys.argv[2:], sys.argv[1])
		else:
			print("[!] Please select at least 2 files to bitwise.")


	elif '-kb' in sys.argv[1]:

		if len(sys.argv[2:]) == 2:
			brute_xor(sys.argv[2], sys.argv[3], sys.argv[1])
		else:
			print("[!] Please select 1 file and set the key to brute-Bitwise with.")


	elif sys.argv[1] == '-u':

		import urllib.request
		try:
			with urllib.request.urlopen('https://raw.githubusercontent.com/JimChr-R4GN4R/TaurusG4T3/main/.last_version') as response:
				print("Last version:",response.read().decode('utf-8'))
		except:
			print('[!] Please check your internet connection or maybe Github is down and the end of the world has started!')
	else:
		print(help_string)

except IndexError:
	print(help_string)
