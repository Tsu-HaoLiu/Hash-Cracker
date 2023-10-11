using System;
using System.Security.Cryptography;
using CSItertools;
using CommandLine;


public static class Globals {
    public static readonly string[] SupportedHashAlgorithms = {
        "md5",
        "sha1",
        "sha256",
        "sha384",
        "sha512"
    };

    public static readonly string ValidLetters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~";

}


public static class HashCracker {
    static string CalculateHash(string input, string hashType) {
        var algorithm = HashAlgorithm.Create(hashType) ?? 
            throw new ArgumentException($"[!] Hash algorithm {hashType} is not supported.");
        var hashBytes = algorithm.ComputeHash(System.Text.Encoding.UTF8.GetBytes(input));

        return BitConverter.ToString(hashBytes).Replace("-", "").ToLower();
    }

    public static string WordlistHash(string hashedString, string hashType, string filePath = "rockyou.txt") {
    
        hashType = hashType.ToLower();
        if (!Globals.SupportedHashAlgorithms.Contains(hashType)) {
            throw new ArgumentException($"[!] Invalid hash type: {hashType}, supported are {string.Join(", ", Globals.SupportedHashAlgorithms)}");
        }

        var totalLines = File.ReadLines(filePath).Count();
        Console.WriteLine($"[*] Cracking hash {hashedString} using [{hashType}] with a list of {totalLines} words.");

        using (var f = File.OpenText(filePath)) {
            string? line;
            while ((line = f.ReadLine()) != null) {
                if (CalculateHash(line, hashType) == hashedString) 
                    return line;
            }
        }

        return "";
    }

    public static string BruteforceHash(string hashedString, string hashType, int minLength = 2, int maxLength = 4) {
        int count = minLength;
        var itertools = new Itertools();

        while (count < maxLength) {
            foreach (var letter in itertools.Product(Globals.ValidLetters, repeat: count)) {
                string joinedString  = string.Join("", letter);
                
                if (CalculateHash(joinedString, hashType) == hashedString) 
                    return joinedString;
            }
        
            count++;
        }

        return "";
    }

}

namespace QuickStart {
    class Program {
        public class Options {
            [Option('s', "hashedString", Required = true, HelpText = "Hash you are looking to crack")]
            public string? HashedString { get; set; }

            [Option('t', "hashedType", Required = true, Default = "md5", HelpText = "Type of hash used")]
            public string? HashedType { get; set; }

            [Option('w', "wordlist", Required = false, Default ="rockyou.txt", HelpText = "Path of wordlist (e.g. C:\\Downloads\\rockyou.txt)")]
            public string? Wordlist { get; set; }

            [Option('b', "bruteforce", Required = false, Default = false, HelpText = "Option to bruteforce the hash")]
            public bool Bruteforce { get; set; }
        }

        static void Main(string[] args) {
            Parser.Default.ParseArguments<Options>(args).WithParsed<Options>( arg => {
                string pw = arg.Bruteforce ? HashCracker.BruteforceHash(arg.HashedString, arg.HashedType) : HashCracker.WordlistHash(arg.HashedString, arg.HashedType, arg.Wordlist);

                if (pw.Length > 0) {
                    Console.WriteLine($"[+] Found password: {pw}");
                    return;
                }
                Console.WriteLine("[-] Cracking Failed");
            });
        }
    }
}
