# OpenBarcodeList V1 
# Tyler Carrothers
# Meant to automate a task of trying to find which barcodes are unavailable and which are.
# Jan 3, 2022 - 6:11 PM
# Build V1 - Avande

import re
# I haven't used regex before, but this is an interesting tool.

def sort_numbers(number_string):
  pattern = r'[\n, ]' # This pattern is all of the things Excel won't filter (and neither will Populi) - line breaks, commas, spaces.
  numbers = [int(x) for x in re.split(pattern, number_string) if x] # Make the variable into a number after splitting it by each delimiter in pattern
  numbers.sort() # Sort alphabetically... more like numerically.
  return numbers # Return the list.

print(""" \n
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
OpenBarcodeList V1 - Created by Tyler Carrothers for BEL REA INSTITUTE OF TECHNOLOGY
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
This program takes your list of barcodes from Populi (take the Excel list of them, 
and just paste the raw data into here (as long as they're numbers only))
and turns the raw data into what barcodes you HAVE used, and the ones you have not.
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

""")

# This section was originally an "input()", but that didn't work as Enter makes this messy.
print("Give me the standard list, and I will convert it. Enter or Paste it, and then Ctrl-C (all operating systems), Ctrl-D or Ctrl-Z (if on Windows) to save it. \n \n")
# Check if there's an EOFError, or a KeyboardInterrupt, and if not, keep accepting data.
numsFilledList = []
while True:
    try:
        line = input()
    except EOFError:
        break
    except KeyboardInterrupt:
        break
    numsFilledList.append(line)
# When done, keep it as a whole list before rejoining.

numsFilled = '\n'.join(numsFilledList) # Rejoin list with line breaks

numList = sort_numbers(numsFilled) # Sort the numbers and make them a list, using a function above.

print("\n \n \n \n Here are the barcodes used in numerical order: \n \n \n \n")

print(numList)
# Print formatted barcode list.

lastNumUnfixed = numList[-1:] # Whatever the highest number in the list is, make it the top bound of this.

# TODO: Allow lastNumUnfixed to be whatever input, but default to numList highest value.

lastNum = int(lastNumUnfixed[0]) # Make list into int

# If you're none of the numbers in this list, be placed into "nonNums" instead. Print "available barcodes" like this.
nonNums = []
for num in range(lastNum + 1):
    if numList.count(num) == 0:
        nonNums.append(num)
print("\n \n \n \n Here are all of the available barcodes: \n \n \n \n")
print(nonNums)
print("\n \n \n \n")