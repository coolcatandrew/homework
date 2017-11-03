#homework from Kira Talent
#Andrew Li
#create a library to help take existing products, repackaging them for sale at electronics stores

markup = {
        'pharmaceutical': 7.5,
        'food':13,
        'electronic': 2
        }


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
    
    if (not numberOfPeople[0:-6].isdigit()):
        print("error - please enter the number of people needed in the format (# people)")
        return -1

    


