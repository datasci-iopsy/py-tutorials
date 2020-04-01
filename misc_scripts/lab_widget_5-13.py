while True: 
    num_wish = input("Enter number of widgets you wish to order: ")

    if num_wish.isdigit() & len(num_wish) == 1:
        print("The subtotal for your order of", num_wish, "widget(s) is $", 
        int(num_wish) * 5)

        while True: 
            choice = input("Do you want express shipping for $5 extra? (Yes or No)") 
            
            if choice not in ("Yes", "y", "yes", "No", "n", "no"): 
                print("We need an answer about express shipping, please!")
                continue
                choice = input("Do you want express shipping for $5 extra? (Yes or No)")
            
            elif choice in ("Yes", "y", "yes"): 
                print("Your order of", num_wish, "widget(s) with express shipping" + 
                " totals to $", (int(num_wish) * 5) + 5)
                break
            else:
                print("Your order of", num_wish, "widget(s) totals to $", 
                (int(num_wish) * 5))
                break
            break
        break
    else:
        print("{} is an invalid input. Please enter 1 through 9!".format(num_wish))
        continue
        break



