from time import sleep
for cont in range(10, -1, -1):
    sleep(1)
    print(cont)
    cont += cont

print('BOW! BOW! POOW!!!')