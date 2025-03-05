Intro = "Kom til 50"
v1 = 5
v2 = 30
v3 = "Hva må du legge til for at summen skal bli 50?"
v4 = v1 + v2

print(Intro)
print("Hvis", v1, "+", v2, "=", str(v4) + ".", "Hvor mye må du legge til?" )
i = int(input(v3))
res = v1 + v2 + i

if res == 50:
    print(True)
    print("Regnestykke blir", res)
else:
    print("Feil!")
