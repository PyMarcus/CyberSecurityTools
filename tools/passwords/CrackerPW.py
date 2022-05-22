import multiprocessing
import string
from itertools import product
from threading import Thread
from passlib.hash import pbkdf2_sha512
from passlib.hash import pbkdf2_sha256
from passlib.hash import md5_crypt
from passlib.hash import pbkdf2_sha1


class CrackerPW:
    def __init__(self, word_from_wordlist: str) -> None:
        self.__word_from_wordlist = word_from_wordlist

    @property
    def word_from_wordlist(self) -> str:
        return self.__word_from_wordlist

    def findCryptPw(self, crypto_pw: str) -> str:
        """
        Try discover encrypted passwords
        :param crypto_pw:
        :return:
        """
        t1: str = pbkdf2_sha1.hash(self.word_from_wordlist)
        t2: str = pbkdf2_sha512.hash(self.word_from_wordlist)
        t3: str = pbkdf2_sha256.hash(self.word_from_wordlist)
        t4: str = md5_crypt.hash(self.word_from_wordlist)
        if hash(crypto_pw) == hash(self.word_from_wordlist): return self.word_from_wordlist
        crypto_pw = pbkdf2_sha256.hash(crypto_pw)

        if crypto_pw == t1:
            return self.word_from_wordlist
        elif crypto_pw == t2:
            return self.word_from_wordlist
        elif crypto_pw == t3:
            return self.word_from_wordlist
        elif crypto_pw == t4:
            return self.word_from_wordlist
        else:
            return "Don´t finded"

    def __bruteForceAttack(self, length_min: int = 0, length: int = 40, default: str = '', specific: bool =False) -> None:
        """
        length = default 10
        default = A, Aa, 1, A1, a1, Aa1, @, A@, a@, 1@, Aa1@
        file_path = 'local do arquivo'
        specific = True if the length is know
        :param length:
        :param default:
        :return:
        """
        alphabet: str = string.ascii_letters
        numbers: str = string.digits
        symbols: str = string.punctuation
        mini: str = string.ascii_lowercase
        upp: str = string.ascii_uppercase
        choice: str = ''
        if default == "A":
            choice = upp
        elif default == "a":
            choice = mini
        elif default == "1":
            choice = numbers
        elif default == "@":
            choice = symbols
        elif default == "Aa":
            choice = alphabet
        elif default == "@a":
            choice = mini + symbols
        elif default == "Aa1@":
            choice = alphabet + numbers + symbols
        elif default == "Aa1":
            choice = alphabet + numbers
        if specific:
            for combinations in product([k for k in choice], repeat=length):
                possible_pw: str = ''.join(combinations)
                print(possible_pw)
        else:
            for x in range(length_min, length):
                for combinations in product([k for k in choice], repeat=x):
                    possible_pw: str = ''.join(combinations)
                    print(possible_pw)

    def bruteForceAttackThreads(self, *args) -> None:
        """
        :param args:
        :return:
        """
        cpu_count: int = multiprocessing.cpu_count()
        threads = [Thread(target=self.__bruteForceAttack, args=(args[0], args[1], args[2] ))]
        [threads[n].start() for n in range(cpu_count)]
        [threads[n].join() for n in range(cpu_count)]

    def runBruteForce(self) -> None:
        process = [
        multiprocessing.Process(target=self.bruteForceAttackThreads, args=(0, 10, "Aa1@", False)),
        multiprocessing.Process(target=self.bruteForceAttackThreads, args=(10, 20, "Aa1@", False)),
        multiprocessing.Process(target=self.bruteForceAttackThreads, args=(20, 30, "1", False)),
        multiprocessing.Process(target=self.bruteForceAttackThreads, args=(30, 60, "@", True))
        ]
        [process[x].start() for x in range(len(process))]
        [process[x].join() for x in range(len(process))]
