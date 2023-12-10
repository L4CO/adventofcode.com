# inporti RegEx module
import re

# open input data file
inputData = open("myDataInput", "r")

# accepted string values representing integers
accepted = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

# result integer
result = 0

# RegEx search pattern
pattern = "\d|" + "|".join(re.escape(word) for word in accepted)

# determine the integer representation for result calculations
def getValue(generalValue):
  # when number (int) representation, then return int value, try to cast into int
  try:
    return str(int(generalValue))
  except:
    # we tried, so its is a word
    dummy = 0

  # when word (strig) representation, then find index in tupple 
  try:
    return str(accepted.index(generalValue) + 1)
  except:
    print("something went wrong")

  # all other are inacceptable
  return "fail"  

# loop trough data file
index = 0

for line in inputData:
    index += 1
    print(index)
    found = re.findall(pattern, line)
    print(line)
    print('found : ' + str(found))
    # concatenate first found and last found digit and add to result as integer
    stringResult = getValue(found[0]) + getValue(found[-1])
    print('String result : ' + stringResult)
    result += int(stringResult)
    print('result : ' + str(result))
    print('+---------------------start from here--------------------------------+')

# print result
print("final result : ", result)

#print RegEx
print(pattern)

# close data file
inputData.close()
