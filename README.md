# TaurusG4T3
TaurusG4T3 is a script in python3 that you can do bitwise operations with all possible values to a file or you can do bitwise operations to many files together. 
After every bitwise operation, binwalk will look for file signatures.


# Installation
Open your terminal and type:
```
git clone https://github.com/JimChr-R4GN4R/TaurusG4T3
cd TaurusG4T3
pip3 install -r requirements.txt
```



# Manual
Brute-Bitwise a file and check for file signatures:
```
python3 TaurusG4T3.py -bx <filename.xyz> # Brute-Xor a file
python3 TaurusG4T3.py -bo <filename.xyz> # Brute-Or a file
python3 TaurusG4T3.py -ba <filename.xyz> # Brute-And a file
```

Bitwise a file with a specific key:
```
python3 TaurusG4T3.py -kbx <filename.xyz> <key> # Xor a file with a specific key
python3 TaurusG4T3.py -kbo <filename.xyz> <key> # Or a file with a specific key
python3 TaurusG4T3.py -kba <filename.xyz> <key> # And a file with a specific key
```

Bitwise many files together and check for file signatures:
```
python3 TaurusG4T3.py -la <filename1.xyz> <filename2.xyz> <filename3.xyz> # Brute-Xor many files together
python3 TaurusG4T3.py -lo <filename1.xyz> <filename2.xyz> <filename3.xyz> # Brute-Or many files together
python3 TaurusG4T3.py -la <filename1.xyz> <filename2.xyz> <filename3.xyz> # Brute-And many files together
```


Check if you have the latest version:
```
python3 TaurusG4T3.py -u
```

# To-Do
[V] Add all bitwise operations.

[V] Update checker

[X] Add custom key for bitwise operations.
