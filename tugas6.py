titik = []

for i in range(3):
    x = float(input(f"x{i+1}: "))
    y = float(input(f"y{i+1}: "))
    titik.append([x,y])
print(titik)
print()

p = ((titik[0][0] - titik[1][0])**2 + (titik[0][1] - titik[1][1]**2))**0.5
q = ((titik[1][0] - titik[2][0])**2 + (titik[1][1] - titik[2][1]**2))**0.5
r = ((titik[0][0] - titik[2][0])**2 + (titik[0][1] - titik[2][1]**2))**0.5

if p == q or q == r or p == r :
    print("ketiga titik membentuk segitiga sama kaki ")
else :
    print("ketiga titik tidak membentuk segitiga sama kaki ")