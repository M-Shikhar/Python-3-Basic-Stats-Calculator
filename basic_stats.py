# define basic_stats function
def basic_stats():
    
    # intro
    print("|------------------------------------------|")
    print("|Hello there! I am a basic stats calculator|")
    print("|------------------------------------------|")
    
    # running program infinitely unless user's choice is 4.End
    while (1):
        print("What do you want to do?\n1.Sum\n2.Average\n3.Frequency of Number in list\n4.End")
        a = input("Pick your choice number\n")
        
        # sum
        if a == "1":
            c = 0
            s = 0
            b = input("Enter numbers for sum.\nIf done, type d\n")
            while b != "d":
                c = c+1
                s = s+int(b)
                b = input("Enter numbers for sum.\nIf done, type d\n")
            if c != 0:
                print("The Result is",s,"!")
            else:
                print("You entered no numbers")
                
        # average       
        elif a == "2":
            s = 0
            c = 0
            b = input("Enter numbers for average.\nIf done, type d\n")
            while b != "d":
                c = c+1
                s = s+int(b)
                b = input("Enter numbers for average.\nIf done, type d\n")
            if c != 0:
                print("The Result is",s/c,"!")
            else:
                print("You entered no numbers")
                
        # list making
        elif a == "3":
            b = []
            b = input("Enter numbers divided by space for list\n").split()
            b = list(map(int, b))
            print("This is your list:\n",b)
            
        # frequency
            c = int(input("Enter the number whose frequency is to be known\n"))
            print("The Frequency is",b.count(c),'!')
        
        # end        
        elif a == "4":
            print("Thankyou for using basic_stats calculator!")
            return()
        
        # invalid option
        else:
            print("That's not a valid option")

# call basic_stats function        
basic_stats()
