#Levelling using height of collimation method
BM = float(input("Enter a benchmark value: "))
print("How many changing point do you have: ")
choice = input()
choice = int(choice)
for i in range(choice):
    print("For changing point",i+1,)
    print("Enter backsite: ")
    BackSite = input()
    BackSite = float(BackSite)
    print("How many intermmediate point do you have? ")
    choice_1 = input()
    choice_1 = int(choice_1)
    for n in range(choice_1):
        print("Enter intermmediate", n+1)
        intermmediate = input()
        intermmediate = float(intermmediate)
        value = BM + BackSite
        value_1 = value - intermmediate
        print(value_1)
    print("Enter a Foresite: ")
    foresite = input()
    foresite = float(foresite)
    value_2 = BM + BackSite - foresite
    print(value_2)
    BM = value_2
                
                
        
    
    