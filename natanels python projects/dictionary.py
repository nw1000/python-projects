monthConversions = {
     "jan": "january",
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sep": "september",
    "oct": "october",
    "nov": "november",
    "dec": "december",
}
try:
    dad = input("enter in a month: ")
    print(monthConversions[dad])
except:
     print("you did not enter in a month")








