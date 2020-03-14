print("--- Permutation Box ---\n\n")

pBox =  [
          ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'],
          ['5','9','C','F','7','0','B','4','E','1','D','6','2','A','8','3']
        ]

print("P-Box:\n")
for i in range(2):
  for j in range(16):
    print(pBox[i][j],end=" ")
  print("")

dataSize = 2
output = ""

print("\n\nSender")
print("------")
input = "B7";
print("Input:",input,end=", ")

for i in range(dataSize):
  for j in range(16):
    if input[i] == pBox[0][j]:
      output += pBox[1][j]

print("Output:",output)


output = ""

print("\n\nReceiver")
print("--------")
input = "64";
print("Input:",input,end=", ")

for i in range(dataSize):
  for j in range(16):
    if input[i] == pBox[0][j]:
      output += pBox[1][j]

print("Output:",output)

print("\n\n")