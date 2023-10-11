# builtin
import hashlib
import string as st
import itertools

# imports
from tqdm import tqdm


def bruteforce_hash(hashed_string: str, hash_type: str = None, min_length: int = 1, max_length: int = 10) -> str | None:
    """Bruteforce hash, speed is depended on your computer hardware
    :param hashed_string: Hash looking to be cracked
    :param hash_type: Type of hash used
    :param min_length: Min length of unhashed string
    :param max_length: Max length of unhashed string
    :return: (string | None) Cracked hash
    """
    word_list: str = st.digits + st.ascii_letters + st.punctuation  # string of possible characters
    count = min_length
    hash_func = getattr(hashlib, hash_type, None)

    # Set a window so it doesn't run forever
    while count < max_length:
        total_chars = pow(len(word_list), count)  # Get the total number of possible combinations
        for letter in tqdm(itertools.product(word_list, repeat=count), desc=f'Bruteforcing hash #{count}', total=total_chars):
            word = ''.join(letter)

            # validate hash then return the correct string
            if hash_func(word.encode()).hexdigest() == hashed_string:
                return word

        count += 1
    return None

def wordlist_hash(hashed_string: str, hash_type: str, wordlist: str) -> str | None:
    """Crack a hash using a wordlist.
    :param hashed_string: Hash looking to be cracked
    :param wordlist: Path to the wordlist
    :param hash_type: Type of hash used
    :return: (string | None) Cracked hash
    """
    hash_type = hash_type.lower()
    hash_func = getattr(hashlib, hash_type, None)
    if hash_func is None or hash_type not in hashlib.algorithms_guaranteed:
        # unsupported hash type
        raise ValueError(f'[!] Invalid hash type: {hash_type}, supported are {hashlib.algorithms_guaranteed}')

    # Count the number of lines in the wordlist to set the total
    total_lines = len(open(wordlist, 'r').readlines())
    print(f"[*] Cracking hash {hashed_string} using [{hash_type}] with a list of {total_lines} words.")

    # open the wordlist
    with open(wordlist, 'r') as f:
        # iterate over each line
        for line in tqdm(f, desc='Cracking hash', total=total_lines):
            if hash_func(line.strip().encode()).hexdigest() == hashed_string:
                return line.strip()
    return None

def arg_parser():
    """Parse commands from CLI """
    import argparse  # only needed if called from CLI

    parse = argparse.ArgumentParser()
    parse.add_argument(
        '-s',
        '--hashed_string',
        type=str,
        required=True,
        help=f'The hash you are looking to crack'
    )
    parse.add_argument(
        '-w',
        '--wordlist',
        type=str,
        help=f'Path of wordlist (e.g. C:\\Downloads\\rockyou.txt)'
    )
    parse.add_argument(
        '-type',
        '--hash_type',
        type=str,
        default='md5',
        help='The hash type used'
    )
    parse.add_argument(
        '-b',
        '--bruteforce',
        action='store_true',
        default=False,
        help='Option to bruteforce the hash'
    )

    args = parse.parse_args()

    pw = bruteforce_hash(hashed_string=args.hashed_string, hash_type=args.hash_type) \
        if args.bruteforce else \
        wordlist_hash(hashed_string=args.hashed_string, wordlist=args.wordlist, hash_type=args.hash_type)

    if pw:
        print(f"[+] Found password: {pw}")
        return
    print("[-] Cracking Failed")


if __name__ == '__main__':
    arg_parser()
    # # if len(sys.argv) > 1:
    # #     arg_parser()
    # # else:
    # # hashname = '5ac2ac5ba94dbce933c6719ca250bf1752d938f43367af6618ab9e9e30b57df701dcda95287c5af56d8374abf292813efa07e1f287b9e4877ff17969b6735fe1'
    # hashname = '314c294196e1d54fcf4612ae1ad7ea62'
    # # named = wordlist_hash(hashname, 'Wordlist.txt', 'sha512')
    # # print("[+] Found password:", named)
    # named = bruteforce_hash(hashname, 'md5')
    # print("[+] Found password:", named)

