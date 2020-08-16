if __name__ == "__main__":
    test_string = 'AweSOME is CoDInG'

    test_list = []

    for i in test_string.split(' '):
        test_list.append(i)

    for e in reversed(test_list):
        print(e.swapcase())