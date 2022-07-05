def swap_case(s):
    return ''.join([i.lower() if i.isupper() else i.upper() for i in             raw_input()])
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
