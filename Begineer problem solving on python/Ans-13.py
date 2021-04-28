def findSubSet(input, n, output):

    if(n < 0):
        output + []
        print(output)
        return

    findSubSet(input, n-1, output)
    findSubSet(input, n-1, output + [input[n]])

inputList = ['v','i','c','k','y']

outputList = []

findSubSet(inputList, len(inputList) - 1 , outputList)