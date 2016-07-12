def separate_number(x):
    while x > 0:
        res = x % 10
        x = x - res
        x = x / 10
        print res

def main():
     data = input("Enter Number:")
     
     separate_number(int(data))


if __name__=='__main__':
    main()


