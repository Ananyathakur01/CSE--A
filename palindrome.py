a=int(input("enter any number\n"))
if a%2==0:
    b=str(a)
    c=(b[::-1])
    if str(a)==c :
        print("it is a palindrome number\n")
    else:
        print("it is not a palindrome number\n")
else:
    print(f"the factorial of {a} is")
    for i in range(1,a+1):
        if a%i==0:
            print(i,end=" ")    
