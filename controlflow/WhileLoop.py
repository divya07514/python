var = 3
while var >= 0:
    print(var)
    var = var - 1
else:
    print("While loop ends here")

print("\n")

intvar = 10
while intvar >= 0:
    if intvar % 2 == 0:
        print(f'Number {intvar} is even')
    else:
        print(f'Number {intvar} is odd')
    intvar = intvar - 1
else:
    print("While loop has ended...")
