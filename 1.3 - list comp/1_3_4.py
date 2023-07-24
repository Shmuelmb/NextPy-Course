import string


def main():
    password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    print("".join([string.ascii_lowercase[string.ascii_lowercase.index(
        i) + 2] if i.isalpha() else i for i in list(password)]))


if __name__ == '__main__':
    main()
