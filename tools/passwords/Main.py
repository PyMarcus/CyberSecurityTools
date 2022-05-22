from CrackerPW import CrackerPW


if __name__ == '__main__':
    cpw = CrackerPW("legal")
    response: str = cpw.findCryptPw("legal")
    print(response)
    cpw.runBruteForce()