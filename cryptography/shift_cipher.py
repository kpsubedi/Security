#!/usr/bin/python
def brute_force():
    for i in range(0,26):
        ans=""
        for j in "helloworldz":
            if ord(j) + i > 122:
                ans = ans + chr((ord(j) + i)%123 + 97)
            else:
	        ans = ans + chr(ord(j) + i)
        print ans, i


def shift_cipher(n):
    ans=""
    for j in "helloworldz":
        if ord(j) + n > 122:
            ans = ans + chr((ord(j) + n)%123 + 97)
        else:
            ans = ans + chr(ord(j) + n)
    print ans, n


if __name__=='__main__':
    brute_force()
    n = raw_input("Please enter a shift amount:")

    shift_cipher(int(n))
