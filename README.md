# Hash-Cracker
Advanced Hash Cracking Tool with support for Bruteforce Attacks, Dictionary Attacks


[Can find rockyou txt file here](https://github.com/danielmiessler/SecLists/tree/master/Passwords)


### C# CLI usage:
```
> HashBuster.exe --help
HashBuster 2023.10.3
Copyright (C) 2023 HashBuster

  -s, --hashedString    Required. Hash you are looking to crack

  -t, --hashedType      Required. (Default: md5) Type of hash used

  -w, --wordlist        (Default: rockyou.txt) Path of wordlist (e.g.
                        C:\Downloads\rockyou.txt)

  -b, --bruteforce      (Default: false) Option to bruteforce the hash

  --help                Display this help screen.

```

Example:
```
> HashBuster.exe -s 0f359740bd1cda994f8b55330c86d845 -t md5 -w rockyou.txt
[*] Cracking hash 0f359740bd1cda994f8b55330c86d845 using [md5] with a list of 999 words.
[+] Found password: p@ssw0rd
```

### Python CLI usage:
```python
python hash_buster.py -s HASHED_STRING [-w WORDLIST] [-type HASH_TYPE] [-b]

options:
  -h, --help            show this help message and exit
  -s HASHED_STRING, --hashed_string HASHED_STRING
                        The hash you are looking to crack
  -w WORDLIST, --wordlist WORDLIST
                        Path of wordlist (e.g. C:\Downloads\rockyou.txt)
  -type HASH_TYPE, --hash_type HASH_TYPE
                        The hash type used
  -b, --bruteforce      Option to bruteforce the hash
```

## Library usage:
```python
from hash_buster import bruteforce_hash, wordlist_hash

hash_string = 'fbc74209d6c21fd434df...'
hash_type = 'sha256'
min_length = 1
max_length = 4
unhashed_string = bruteforce_hash(hash_string, hash_type, min_length, max_length)
print(unhashed_string) 

# ----------------

hash_string = '5ac2ac5ba94dbce933c671...'
hash_type = 'sha512'
file_path = 'rockyou.txt'
unhashed_string = wordlist_hash(hash_string, hash_type, file_path)
print(unhashed_string) 
```
