num=int(input("Enter a Number : "))

if (num>=0 and num<31):
    print(f"Table of powers of 2 up to 2^{num}:")
    for i in range(num + 1):
        print(f"2^{i} = {2**i}")
else:
    print("Enter Valid Number between 0-30")