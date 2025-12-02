with open("DAY-1/input.txt", "r", encoding="utf-8") as f:
    input_text = f.read()
    input_text = input_text.replace('L','-')
    input_text = input_text.replace('R','')
    input_lines = input_text.splitlines()
dial = 50
nb_zero = 0
print("Méthode with dial adjustment")
for line in input_lines:
    if int(line) >= 0:
        dial += int(line)%100
    else:
        dial += (int(line)%100)-100
    
    if dial < 0:
        dial += 100
    elif dial >= 100:
        dial -= 100
    if dial == 0:
        nb_zero += 1
print(nb_zero)
print("Méthode without dial adjustment")
for line in input_lines:
    dial += int(line)%100
    if dial == 0:
        nb_zero += 1
print(nb_zero)

