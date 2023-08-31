

def main():
    numbers = iter(list(range(1, 101)))

    while True:
        try:
            next(numbers)
            print(next(numbers))
        except:
            break


if __name__ == '__main__':
    main()
