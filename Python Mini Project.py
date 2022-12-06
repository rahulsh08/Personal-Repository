a = input("Numbers of cuts (As Integer): ")
ANGLES_IN_LIST = list(map(int,input("Angles with sep.. comma (As Integer): ").split(',')))

sumAngle = 0
for i in ANGLES_IN_LIST:
    sumAngle = sumAngle + i

if sumAngle == 360:

    b = ["0","1","2","3","4","5","6","7","8","9"]
    c = ""

    for i in range(len(a)):
        if a[i] in b:
            c = c + a[i]
        else:
            continue   
        
    k = []

    if  len(a) == len(c):
        NUMBER_OF_CUTS = int(a)
        for i in ANGLES_IN_LIST:
            if i not in k:
                k.append(i)
        
        if NUMBER_OF_CUTS ==len(ANGLES_IN_LIST) and sumAngle == 360:
            if len(k) == 1 and k[0] * NUMBER_OF_CUTS == 360 and len(ANGLES_IN_LIST) == NUMBER_OF_CUTS:
                print("First case satisfied")
            else:
                print("First case not satisfied")
            if sumAngle == 360 and len(ANGLES_IN_LIST) == NUMBER_OF_CUTS:
                print("Second case satisfied")
            else:
                print("Second case not satisfied")
            if k == ANGLES_IN_LIST:
                print("Third case satisfied")
            else:
                print("Third case not satisfied")
        else:
            print("Give me correct input.....")    

    else:
        print("Entered number is not integer...")
else:
    print("Given angle is not add up to 360")