#homework from Kira Talent
#Andrew Li
#create a library to help take existing products, repackaging them for sale at electronics stores

#function to take in the base item price, the number of people who need to work on the item, and the item type and return a float as the final price after the markup
#returns -1 after printing error if occurs
#params: 
#    float basePrice,
#    string numberOfPeople (n followed by people, eg 0 people, 1 person, 2 people, etc)
#    string itemType
def calculateMarkup(basePrice, numberOfPeople, itemType):
    #validate input
    if (not isinstance(basePrice, float)):
        print("error - basePrice is not a float")
        return -1
    
    if (not numberOfPeople[0:-7].isdigit()):
        print("error - please enter the number of people needed in the format (# people)")
        return -1
    
    #start calculations
    #uncomment print statements for more accurate information
    print("Base Price:     %.2f"% basePrice)
    print("Flat Markup:    5% =","%.4f"% (float(basePrice*0.05))) 
    subtotal = float(basePrice*1.05)
    print("Subtotal:       %.4f"% subtotal)
    
    numberOfPeople = int(numberOfPeople[0:-7])
    peopleMarkup = float(0.012 * numberOfPeople)
    peopleSubtotal = float(peopleMarkup * subtotal)
    print("Person Markup:  %d"% numberOfPeople, "* 1.2% =","%.1f = %.6f"% (peopleMarkup * 100, peopleSubtotal))
    
    typeMarkup = 0.0

    if (itemType.lower() == "pharmaceutical"):
        typeMarkup = 0.075
    elif (itemType.lower() == "food"):
        typeMarkup = 0.13
    elif (itemType.lower() == "electronic"):
        typeMarkup = 0.02
    typeSubtotal = float(typeMarkup * subtotal)
    #print("Type Markup:   %.1f" % (typeMarkup * 100), "%" , " = %.6f" % float(typeMarkup * subtotal))

    total=subtotal + typeSubtotal + peopleSubtotal
    print("Total:          %.6f" % total)
    round(total, 2)
    return (total)



print(calculateMarkup(1299.99,"3 people", "food"))
