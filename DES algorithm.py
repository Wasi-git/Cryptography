print("--- DES Algorithm ---\n\n")

sBox =  [
          ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'],
          ['5','9','C','F','7','0','B','4','E','1','D','6','2','A','8','3'],
          ['1','9','A','B','C','D','E','F','0','1','2','3','4','5','6','7'],
          ['A','B','C','5','E','F','D','1','2','3','4','6','2','A','8','3'],
          ['0','1','C','F','7','2','B','4','E','1','D','6','2','C','A','B']
        ]

print("S-Box:\n")
for i in range(5):
  for j in range(16):
    print(sBox[i][j],end=" ")
  print("")

input = "101101";
print("\n\nInput:",input)

row = int(input[0:2], 2)
column = int(input[2:], 2)
output = format(int(sBox[row][column],16),"04b")
#output = bin(int(sBox[row][column],16)).replace("0b","")
print("\nOutput:",output)

print("\n\n");
