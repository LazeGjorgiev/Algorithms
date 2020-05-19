from GeometricAlgorithmsProject.Zemjodelec import Zemjodelec

print("EXAMPLE 1")
print("INPUT")
print("7\n\
3 2\n\
1 3\n\
6 6\n\
7 9\n\
4 10\n\
2 8\n\
6 3\n\
4\n\
11 2\n\
12 5\n\
12 9\n\
11 10\n")

print("EXPECTED OUTPUT: ")
print("45.0")
print("RECEIVED OUTPUT:")
outptu1 = Zemjodelec().povrsina_na_sosednata_niva(7,
        ["3 2","1 3","6 6","7 9","4 10","2 8","6 3"],4,
      ["11 2","12 5","12 9","11 10"])

print(outptu1)
print(str(outptu1) == "45.0")
print()

print("EXAMPLE 2")
print("INPUT")
print("10\n\
1 2\n\
5 3\n\
10 6\n\
3 9\n\
7 10\n\
11 8\n\
0 3\n\
3 10\n\
4 3\n\
5 0\n\
5\n\
11 4\n\
14 5\n\
12 9\n\
13 10\n\
11 10\n")

print("EXPECTED OUTPUT: ")
print("31.0")
print("RECEIVED OUTPUT:")
outptu1 = Zemjodelec().povrsina_na_sosednata_niva(10,
        ["1 2","5 3","10 6","3 9","7 10","11 8","0 3","3 10","4 3","5 0"],5,
      ["11 4","14 5","12 9","13 10","11 10"])

print(outptu1)
print(str(outptu1) == "31.0")
print()

print("EXAMPLE 3")
print("INPUT")
print("7\n\
1 2\n\
4 3\n\
8 6\n\
3 9\n\
4 10\n\
2 8\n\
6 3\n\
3\n\
8 6\n\
6 3\n\
4 4\n")

print("EXPECTED OUTPUT: ")
print("0.0")
print("RECEIVED OUTPUT:")
outptu1 = Zemjodelec().povrsina_na_sosednata_niva(7,
        ["1 2","4 3","8 6","3 9","4 10","2 8","6 3"],3,
      ["8 6","6 3","4 4"])

print(outptu1)
print(str(outptu1) == "0.0")
