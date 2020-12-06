# TaurusG4T3
TaurusG4T3 is a script in python3 that you can do bitwise operations with all possible values on a file or you can do bitwise operations on many files together. 
After every bitwise operation, binwalk will look for file signatures.


# Installation
open your terminal and type:
```
git clone https://github.com/JimChr-R4GN4R/TaurusG4T3
cd TaurusG4T3
pip3 install -r requirements.txt
```



# Manual
Brute-Bitwise a file and check for file signatures:
```
python3 TaurusG4T3.py -bx <filename.xyz>
python3 TaurusG4T3.py -bo <filename.xyz>
python3 TaurusG4T3.py -ba <filename.xyz>
```



Bitwise many files together and check for file signatures:
```
python3 TaurusG4T3.py -la <filename1.xyz> <filename2.xyz> <filename3.xyz>
python3 TaurusG4T3.py -lo <filename1.xyz> <filename2.xyz> <filename3.xyz>
python3 TaurusG4T3.py -la <filename1.xyz> <filename2.xyz> <filename3.xyz>
```

# To-Do
[V] Add all bitwise operations.
