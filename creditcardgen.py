import copy
from random import Random

visaPrefixList = [
    ['4', '5', '3', '9'],
    ['4', '5', '5', '6'],
    ['4', '9', '1', '6'],
    ['4', '5', '3', '2'],
    ['4', '9', '2', '9'],
    ['4', '0', '2', '4', '0', '0', '7', '1'],
    ['4', '4', '8', '6'],
    ['4', '7', '1', '6'],
    ['4']]

mastercardPrefixList = [
    ['5', '1'], ['5', '2'], ['5', '3'], ['5', '4'], ['5', '5']]

amexPrefixList = [['3', '4'], ['3', '7']]

discoverPrefixList = [['6', '0', '1', '1']]

dinersPrefixList = [
    ['3', '0', '0'],
    ['3', '0', '1'],
    ['3', '0', '2'],
    ['3', '0', '3'],
    ['3', '6'],
    ['3', '8']]

enRoutePrefixList = [['2', '0', '1', '4'], ['2', '1', '4', '9']]

jcbPrefixList = [['3', '5']]

voyagerPrefixList = [['8', '6', '9', '9']]


def completed_number(prefix, length):
    """
    'prefix' is the start of the CC number as a string, any number of digits.
    'length' is the length of the CC number to generate. Typically 13 or 16
    """

    ccnumber = prefix

    # generate digits

    while len(ccnumber) < (length - 1):
        digit = str(generator.choice(range(0, 10)))
        ccnumber.append(digit)

    # Calculate sum

    sum = 0
    pos = 0

    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()

    while pos < length - 1:

        odd = int(reversedCCnumber[pos]) * 2
        if odd > 9:
            odd -= 9

        sum += odd

        if pos != (length - 2):
            sum += int(reversedCCnumber[pos + 1])

        pos += 2

    # Calculate check digit

    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10

    ccnumber.append(str(checkdigit))

    return ''.join(ccnumber)


def credit_card_number(rnd, prefixList, length, howMany):
    result = []

    while len(result) < howMany:
        ccnumber = copy.copy(rnd.choice(prefixList))
        result.append(completed_number(ccnumber, length))

    return result


def output(title, numbers):
    result = []
    result.append(title)
    result.append('-' * len(title))
    result.append('\n'.join(numbers))
    result.append('')

    return '\n'.join(result)


#
# Main
#

generator = Random()
generator.seed()  # Seed from current time

print("CREDIT CARD NUMBER(S) GENERATOR\n")
print("Card types supported:\n")
print("1. Mastercard")
print("2. Visa (16)")
print("3. Visa (13)")
print("4. American Express")
print("5. Discover")
print("6. Diners\n")
type1 = int(input("Enter card type (no. from the above list): "))
type2 = int(input("Enter no. of cards required: "))

if type1 == 1:
    mastercard = credit_card_number(generator, mastercardPrefixList, 16, type2)
    print(output("Mastercard", mastercard))

if type1 == 2:
    visa16 = credit_card_number(generator, visaPrefixList, 16, type2)
    print(output("VISA 16 Digit", visa16))

if type1 == 3:
    visa13 = credit_card_number(generator, visaPrefixList, 13, type2)
    print(output("VISA 13 digit", visa13))

if type1 == 4:
    amex = credit_card_number(generator, amexPrefixList, 15, type2)
    print(output("American Express", amex))

if type1 == 5:
    discover = credit_card_number(generator, discoverPrefixList, 16, type2)
    print(output("Discover", discover))

if type1 == 6:
    diners = credit_card_number(generator, dinersPrefixList, 14, type2)
    print(output("Diners Club / Carte Blanche", diners))

print("Thanks for using our service.")

