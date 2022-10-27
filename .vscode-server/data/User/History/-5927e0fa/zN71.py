alfabeto = ["a", "b", "c", "d", "e", "f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
int(alfabeto)
for i in alfabeto:
    if i % 2 == 0:
        print(i)    
    else:
        alfabeto.pop(i)