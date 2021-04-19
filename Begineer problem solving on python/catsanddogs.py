# cook your dish here

testcases = int(input())

for t in range(0, testcases):

    inp = input().split(" ")
    cats = int(inp[0])
    dogs = int(inp[1])
    lags = int(inp[2])

    animalCount = lags/4
    totalCatsAndDogs = cats + dogs
    catsOnGround = animalCount - dogs
    catsOnDogs = cats - catsOnGround

    if(lags%4 != 0):
        print("no")
        continue

    if(animalCount < dogs):
        print("no")
        continue

    if(totalCatsAndDogs < animalCount):
        print("no")
        continue

    if(catsOnDogs > dogs*2):
        print("no")
        continue

    print("yes")