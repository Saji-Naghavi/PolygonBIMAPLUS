# Polygon Info
print("The number of polygon edges: ")
PointNumber= int (input())

Xlist = []
Ylist = []

print()
# print("Enter x and y coordinates for polygon points ...")
for i in range(PointNumber):
    print (f"please enter X Point No.{i+1}: ")
    x=float(input())
    Xlist.append(x)
    print (f"please enter Y {i+1}: ")
    y=float(input())
    Ylist.append(y)
   
print(Xlist)
print(Ylist)

# Print table to screen

print()
print(f"{'Point No.':15} {'Xlist':15} {'Ylist':15}")
print("=" * 40)
for i in range(PointNumber):
    print(f"{i+1:<15d} {Xlist[i]:<15.2f} {Ylist[i]:<15.2f}")

# result

print ()
print ()

ToAX = 0
for i in range(PointNumber-1):
    ToAX +=(Xlist[i+1]+Xlist[i])*(Ylist[i+1]-Ylist[i])
AX = ToAX/2
print (f"AX = {AX: .2f}")

ToSX = 0
for i in range(PointNumber-1):
    ToSX +=(Xlist[i+1] - Xlist[i])*(Ylist[i+1]**2 + Ylist[i] * Ylist[i+1] + Ylist[i]**2)
SX = ToSX/-6
print (f"SX = {SX: .2f}")

ToSY = 0
for i in range(PointNumber-1):
    ToSY +=(Ylist[i+1] - Ylist[i]) * (Xlist[i+1]**2 + Xlist[i] * Xlist[i+1] + Xlist[i]**2)
SY = ToSY/6
print (f"SY = {SY: .2f}")

ToIX = 0
for i in range(PointNumber-1):
    ToIX +=(Xlist[i+1] - Xlist[i]) * (Ylist[i+1]**3 + Ylist[i+1]**2 * Ylist[i] + Ylist[i+1] * Ylist[i]**2 + Ylist[i]**3)
IX = ToIX/-12
print (f"IX = {IX: .2f}")

ToIY = 0
for i in range(PointNumber-1):
    ToIY +=(Ylist[i+1] - Ylist[i]) * (Xlist[i+1]**3 + Xlist[i+1]**2 * Xlist[i] + Xlist[i+1] * Xlist[i]**2 + Xlist[i]**3)
IY = ToIY/12
print (f"IY = {IY: .2f}")

XT = SY/AX
print (f"XT = {XT: .2f}")

YT = SX/AX
print (f"YT = {YT: .2f}")

ITX = IX - YT**2 * AX
print (f"ITX = {ITX: .2f}")

ITY = IY - XT**2 * AX
print (f"ITY = {ITY: .2f}")