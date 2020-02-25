import math


def huffmann(given_list):

    #def variables
    rem_1 = 1
    resultList = []
    pointer = 0

    #if empty list is entered
    if not given_list:
        stack = []
        i = 0

        print("\n -------------- START ---------------- \n")
        print("Once remaining probability is equal to 0, Algorithm will start \n" )

        #take input
        while True:
            

            #input of decimal and character is saved as as stack, with the second part being a list containing the string: [decimal , ["string"]]. This is used later to be able to
            #assign the 0 and 1 to the correct characters.
            dec = float(input("input decimal: "))
            cha = input("pls: ")



            newTuple = [dec,cha]

            stack.append(newTuple)
            


            #check if probability more than 1
            if rem_1 - stack[i][0] > 1:
                del stack[i]

                print("Your total percentage adds up to more than 1, please reconsider!")

            #start huffmann if remainder == 0
            elif rem_1 == 0:
                break

            #reduce remainder
            else:
                #reduce total remainder
                rem_1 = rem_1 - stack[i][0]

                #increment iterator
                i = i + 1


            print("Amount of remaining probability: " + str(rem_1) + "\n")


    #using given_list
    else:
        stack = given_list

    #sort the stack in descending order
    stack.sort(reverse = True) 

    

    #Kodierung: for every element of the list, 
    for l in range(len(stack)-1):

        print("stack: " + str(stack))
        #nimm die 2 kleinsten elemente (also die mit der kleinsten wahrscheinlichkeit)
        y_1 = stack.pop()
        y_2 = stack.pop()

        #zur uebersicht
        print("New element: " + str(( round( y_2[0] + y_1[0] , 4) , False)) + "\n")

        #1. Fall, beide elemente sind noch nicht in der resultList
        if len(y_1[1]) == 1 and len(y_2[1]) == 1: 
            stack.append(( math.ceil( y_2[0] + y_1[0] , 4) , [pointer , pointer+1]))

            print("lol" + str([pointer, pointer + 1]))
            #pointer um 2 incrementieren, weil die 2 pointer die gesetzt wurden auf ihre zugehoerigen elemente in der resultList zeigen
            pointer = pointer + 2

            resultList.append((y_1[1],["0"]))
            resultList.append((y_2[1],["1"]))

        #2. Fall, y_1 ist ein knoten der aus mehr als einem element besteht, und dessen einzelne elemente schon in der resultList stehen. y_2 ist noch nicht in der resultList
        if len(y_1[1]) > 1 and len(y_2[1]) == 1: 
            stack.append(( math.ceil( y_2[0] + y_1[0] , 4) , y_1[1] + [pointer]))
            pointer = pointer + 1

            #fuer jeden pointer in 
            for m in y_1[1]:
                resultList[m][1].append("0")

            resultList.append((y_2[1],["1"]))     

        #3. Fall, y_2 ist ein knoten der aus mehr als einem element besteht, und dessen einzelne elemente schon in der resultList stehen. y_1 ist noch nicht in der resultList
        if len(y_1[1]) == 1 and len(y_2[1]) > 1: 
            stack.append(( round( y_2[0] + y_1[0] , 4) , y_2[1] + [pointer]))
            pointer = pointer + 1

            resultList.append((y_1[1],["0"]))

            #fuer jeden pointer in 
            for m in y_2[1]:
                resultList[m][1].append("1")



        #4. Fall, y_1 und y_2 sind knoten die aus mehr als einem element bestehen, und dessen einzelne elemente schon in der resultList stehen.
        if len(y_1[1]) > 1 and len(y_2[1]) > 1: 
            stack.append(( round( y_2[0] + y_1[0] , 4) , y_1[1] + [pointer]))
            pointer = pointer + 1

            #fuer jeden pointer in 
            for n in y_1[1]:
                resultList[n][1].append("0")

            #fuer jeden pointer in 
            for m in y_2[1]:
                resultList[m][1].append("1")

        
        #stack neu sortieren
        stack.sort(reverse = True)

        print("resultList: " + str(resultList) + "\n")

    return resultList


#zum testen:
probablities = [(0.1,"a"),(0.2,"b"),(0.2,"c"),(0.21,"d"),(0.29,"e")]


huffmann(probablities)

huffmann([])




