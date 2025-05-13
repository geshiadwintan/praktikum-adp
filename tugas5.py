nilai_x = [i for i in range(-7,7+1)]
n = len(nilai_x)
f_x = []

for i in nilai_x :
    if i > 0 :
        fx = i**3 - i
    elif i<0 :
        fx = 1/(i**2)
    else :
        fx = 1
    f_x.append(fx)

print("   TABEL FUNGSI f(x)   ")
print("|   x  |     f(x)   |")
print("|-------------------|")

for i in range (n):
    print(f"| {nilai_x[i]:>3}  | {f_x[i]:>10.5f} |")

