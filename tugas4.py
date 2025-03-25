n = int(input("input n: "))
total_boom = 0  

if n<4:
    print("n minimal berjumlah 4")
else:
    for i in range(n):
        for j in range(n):
            if n % 2 == 1 and i == j == n//2:
                print(" HORE", end=" ")
            elif i == j:
                print("  1  ", end=" ")
            elif i + j == n - 1:
                print("  2  ", end=" ")
            else:
                print(" BOOM", end =" ")
                total_boom +=1
        print()

print(f"Total boom yang muncul sebanyak = {total_boom}")