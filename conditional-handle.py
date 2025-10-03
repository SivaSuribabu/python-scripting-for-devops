import sys
type = sys.argv[1]

if type == "t2.medium":
    print("ok, we are creating the t2.medium instance , it will charge 2 dollars per day")

elif type == "t2.large":
    print("ok, we are creating the t2.large instance , it will charge 4 dollars per day")

elif type == "t2.xlarge":
    print("ok, we are creating the t2.xlarge instance , it will charge 8 dollars per day")

elif type == "t2.2xlarge":
    print("ok, we are creating the t2.2xlarge instance , it will charge 16 dollars per day")

elif type == "m1.medium":
    print("ok, we are creating the m1.medium instance , it will charge 10 dollars per day")

elif type == "m1.large":
    print("ok, we are creating the m1.large instance , it will charge 20 dollars per day")

else:
    print("we are not supporting this instance right now, please try again later")