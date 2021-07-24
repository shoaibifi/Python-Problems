a = [1,2,3,4,5,6,7,89,33,22,34,23,233,5,2,4,8,1,23,12]
evens = 0
odds = 0
for i in a:
    if i%2==0:
        evens+=1
    else:
        odds +=1
print("Odds",odds)
print("Evens",evens)
