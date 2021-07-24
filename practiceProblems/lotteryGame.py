choice = "y"
while choice =="y" or choice =="Y":


    import random
    lottery_number = []
    for i in range(1,6):
        number = random.randint(1,40)
        lottery_number.append(number)

    def fun(l):
        correct = 0
        sorted_list = []
        while l:
            max = l[0]
            for i in l:
                if i > max:
                    max = i
            sorted_list.append(max)
            l.remove(max)

        user = []
        for i in range (len(sorted_list)):
            num = int(input("enter the number :"))
            user.append(num)

        for i in range (0,5):
            if user[i] == sorted_list[i]:
                correct += 1
            

        if correct == 5:
            print("you win")
        else:
            print("you lose")
            print("LOTTERY NUMBER")
            for j in sorted_list:
                print(j,end="")
    fun(lottery_number)
    choice = input("DO YOU WANT TO CONTINUE THE GAME! Y/N")

