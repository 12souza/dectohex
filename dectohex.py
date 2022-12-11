sx = int(input("Put in a numerical value to get its hexadecimal value... "))

remainders = []
hexCodes = {0:"0",
            1:"1",
            2:"2",
            3:"3",
            4:"4",
            5:"5",
            6:"6",
            7:"7",
            8:"8",
            9:"9",
            10:"A",
            11:"B",
            12:"C",
            13:"D",
            14:"E",
            15:"F",
            }
x = sx
while x > 0:
    ivx = x
    r = x % 16
    x = x // 16
    remainders.append(r)
    print(f"{ivx} // 16 == {x}\n{ivx} % 16 = {r}\n\n")
    
remainders = list(reversed(remainders))
for i in remainders:
    idx = remainders.index(i)
    remainders[idx] = hexCodes[i]

hexadecimal = "".join(remainders) 
print(f"{sx} in hexadecimal form is {hexadecimal}")
