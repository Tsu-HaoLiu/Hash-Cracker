# Hash-Cracker C#
Advanced Hash Cracking Tool with support for Bruteforce Attacks, Dictionary Attacks


[Can find rock you txt file here](https://github.com/danielmiessler/SecLists/tree/master/Passwords)


### C# CLI usage:
```csharp
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

## Library usage:
```csharp
using static HashBuster;

string hash = "3e52b22ebfaa4ec...";
string hashType = "md5";
int minLength = 1;
int maxLength = 5;
var crackedHash = HashBuster.BruteforceHash(hash, hashType, minLength, maxLength);
Console.WriteLine(crackedHash);

# ----------------

string hash = "a075d17f3d453073853f...";
string hashType = "sha256";
string filePath = "rockyou.txt";
var crackedHash = HashBuster.WordlistHash(hash, hashType, filePath);
Console.WriteLine(crackedHash);
```
