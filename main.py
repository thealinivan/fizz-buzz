def FizzBuzz (numbersRange, numbersDictionary):

    output = ""
    for numR in numbersRange:
        for numD in numbersDictionary:
            if numR % numD == 0:
                output += numbersDictionary[numD]
        print(output)
        output = ""


numberArray = range(1,50)
quotingDict = {3:"Fizz", 5:"Buzz", 7:"Neeze"}

FizzBuzz(numberArray, quotingDict)


