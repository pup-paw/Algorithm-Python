a = int(input())
b = int(input())
if a >= b:
    print("Congratulations, you are within the speed limit!")
    exit()
elif b-a <= 20:
    f = 100
elif b-a <= 30:
    f = 270
else:
    f = 500
print("You are speeding and your fine is ${}.".format(f))
