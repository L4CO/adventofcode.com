# inporti RegEx module
import re

# open input data file
inputData = open("myDataInput", "r")

# accepted string values representing integers
accepted = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# result integer
result = 0

# RegEx search pattern
pattern = '\d|' + '|'.join(re.escape(word) for word in accepted)

# determine the integer representation for result calculations
def getValue(generalValue):
  # when int, then return int value, try to cast into int
  try:
    print(int(generalValue))
    return str(generalValue)
  except:
    #do nothong
    a = 1

  # when strig representation, then find index in tupple 
  try:
    print(accepted.index(str(generalValue)) + 1)
    return str(accepted.index(str(generalValue))) + 1
  except:
    #do nothond
    b = 1

  # all other are inacceptable
  return '0'  

# loop trough data file
for line in inputData:
    found = re.findall(pattern, line)
    #\b(one|two)\b
    # concatenate first found and last found digit and add to result as integer
    stringResult = getValue(found[0]) + getValue(found[-1])
    print('String result : ' + stringResult)
    result += int(stringResult)
    #result += int(getValue(found[0]) + getValue(found[-1]))
    print('line : ' + line)
    print('found : ' + str(found))
    print('result : ' + str(result))

# print result
print("final result : ", result)
print(pattern)

# close data file
inputData.close()
