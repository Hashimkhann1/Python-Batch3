def ascii_sum(s):
    a=0
    for i in range(len(s)):
        b=(ord(s[i]))
        a=a+b
    print("sum of ascii",a)

def ascii_sum_odd(s):
    a=0
    for i in range(len(s)):
        b=ord(s[i])
        if b%2==1:
            a=a+b
    print("sum of odd ascii",a)


def ascii_sum_even(s):
    a = 0
    for i in range(len(s)):
        b = ord(s[i])
        if b%2==0:
            a=a+b
    print("the sum of even ascii",a)

a = input("enter the string")
ascii_sum(a)
ascii_sum_odd(a)
ascii_sum_even(a)