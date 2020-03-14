hexInput = "32f21bcf"
print("hexInput:",hexInput)
intInput= int(hexInput,16)
binaryInput = format(intInput,"032b")
print("binaryInput:",binaryInput)

middleOfBit = int(len(binaryInput) / 2)
print("middleOfBit:",middleOfBit)

binaryLeft = binaryInput[0:middleOfBit]
binaryRight = binaryInput[middleOfBit:]
print("\nbinaryLeft:",binaryLeft)
print("binaryRight:",binaryRight)

hexKey = "ab56"
print("\nhexKey:",hexKey)
intKey= int(hexKey,16)
binaryKey = format(intKey,"016b")
print("binaryKey:",binaryKey)

xnorResult = ""

def XNOR(right, key):
  global xnorResult
  if(right == key):
    xnorResult += "1"
  else:
    xnorResult += "0"

for i in range(middleOfBit):
  XNOR(binaryRight[i], binaryKey[i])

print("\nxnorResult:",xnorResult)

xorResult = ""

def XOR(left, xnorResult):
  global xorResult
  if(left == xnorResult):
    xorResult += "0"
  else:
    xorResult += "1"

for i in range(middleOfBit):
  XOR(binaryLeft[i], xnorResult[i])

print("xorResult:",xorResult)

xorIntResult = int(xorResult,2)
xorHexResult = hex(xorIntResult).replace("0x","")
print("\nxorHexResult:",xorHexResult)

hexResult = hexInput[4:] + xorHexResult
print("hexResult:",hexResult)