"""
homework from Kira Talent
Andrew Li
create a library to help take existing products, repackaging them for sale at electronics stores
"""
class PricePackager:
    __itemMarkup = 0.0 #no markup initially
    __baseMarkup = 1.05 #5% base markup
    __peopleMarkup = 0.0 #no markup initially
    __markupPerPerson = 0.012 #1.2% markup per person working on product
    __numberOfPeople = "0 people"
    __itemType = ""
    __basePrice = 0.00
    __subTotal = 0.0
    __totalPrice = 0.0

    __markups = {"electronic": 0.02, #2% markup for electronic
                 "food":0.13, #13% markup for food
                 "pharmaceutical": 0.075} #7.5% markup for pharmaceuticals

    """
    Constructor to take in the base item price, the number of people who need to work on the item, and the item type and prints a float as the final price after the markup
    Params:
        float basePrice,
        string numberOfPeople (n followed by people, eg 0 people, 1 person, 2 people, etc)
        string itemType
    """ 
    def  __init__(self, basePrice, numberOfPeople, itemType):
        validInput = False
        if self.validateFloat(basePrice) and self.validateNumberOfPeople(numberOfPeople):
            validInput = True
        if (validInput):
            self.__basePrice = basePrice
            self.__numberOfPeople = numberOfPeople
            self.__itemType = itemType
            self.__subTotal = basePrice * self.__baseMarkup
            self.__itemMarkup = self.getItemMarkup() + self.getItemMarkupFromItemType(itemType)
            self.__peopleMarkup = self.getPeopleMarkup() + self.getPeopleMarkupFromNumberOfPeople(numberOfPeople)
            self.__total = self.calculateTotal(self.__subTotal, self.__peopleMarkup, self.__itemMarkup)
            print(round(self.__total,2))
        else:
            print("Invalid input - Cannot calculate price markup")
            

    def validateFloat(self, floatToCheck):
        if (not isinstance(floatToCheck, float)):
            print("error - basePrice is not a float")
            return False
        return True
            
    def validateNumberOfPeople(self, numberOfPeople):
        if (not numberOfPeople[0:-7].isdigit()):
            print("error - please enter the number of people needed in the format (# people)")
            return False
        return True

    def getItemMarkup(self):
        return self.__itemMarkup

    def getPeopleMarkup(self):
        return self.__peopleMarkup

    def getMarkupDict(self):
        return self.__markups

    def getItemMarkupFromItemType(self, itemType):
        markupDicts = self.getMarkupDict()
        for key in markupDicts.keys():
            if itemType.lower() == key:
                return markupDicts[key]
            return 0

    def getPeopleMarkupFromNumberOfPeople(self, numberOfPeopleString):
        numberOfPeople = int(numberOfPeopleString[0:-7])
        return numberOfPeople * self.__markupPerPerson

    def calculateTotal(self, subTotal, personMarkup, itemMarkup):
        personSubtotal = subTotal * personMarkup
        itemSubtotal = subTotal * itemMarkup
        return subTotal + personSubtotal + itemSubtotal
    

