class SwapingFile:

    def swapFileData():
        input1 = input("Enter the file that you want to swap: ")
        input2 = input("Enter the file in which you want to swap the first file: ")

        with open(input1, 'r') as a:
            data_a = a.read()

        with open(input2, 'r') as a:
            data_b = a.read()

        with open(input1, 'w') as a:
            a.write(data_b)
        
        with open(input2, 'w') as a:
            a.write(data_a)

    swapFileData()
        