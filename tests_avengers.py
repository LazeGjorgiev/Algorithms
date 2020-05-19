######### 1 #########
from GeometricAlgorithmsProject.Avengers import Avengers

print("EXAMPLE 1")
print("INPUT")
print("8\n\
1 1\n\
2 5\n\
1 6\n\
8 7\n\
3 6\n\
6 5\n\
6 6\n\
8 2\n\
5\n\
2 3\n\
6 8\n\
6 6\n\
1 4\n\
10 8\n\
3\n")

print("EXPECTED OUTPUT: ")
print("4 6-8 L 2-5 8-7 3-6 6-6")
print("RECEIVED OUTPUT:")
outptu1 = Avengers().destroyed_planets(
        [(1,1),(2,5),(1,6),(8,7),(3,6),(6,5),(6,6),(8,2)],
      [(2,3),(6,8),(6,6),(1,4),(10,8)], 3)

print(outptu1)
print(outptu1 == "4 6-8 L 2-5 8-7 3-6 6-6")
print()

print("EXAMPLE 2")
print("INPUT")
print("16\
13 6\
16 6\
1 9\
7 18\
12 22\
10 20\
29 5\
24 21\
4 21\
3 20\
11 14\
25 16\
23 23\
7 8\
1 16\
10 21\
16\
1 1\
5 6\
29 0\
28 5\
30 20\
23 25\
16 23\
10 15\
3 10\
-1 13\
0 5\
5 20\
4 19\
10 0\
15 24\
31 5\
3")

print("EXPECTED OUTPUT: ")
print("16 4-19 U 13-6 16-6 1-9 7-18 12-22 10-20 29-5 24-21 4-21 3-20 11-14 25-16 23-23 7-8 1-16 10-21")
print("RECEIVED OUTPUT:")
outptu1 = Avengers().destroyed_planets(
        [(13, 6), (16, 6), (1, 9), (7, 18), (12, 22), (10, 20), (29, 5), (24, 21), (4,21),(3, 20), (11, 14), (25, 16), (23, 23), (7, 8), (1, 16), (10, 21)],
      [(1,1),(5,6),(29,0),(28,5),(30,20),(23,25),(16,23),(10,15),(3,10),(-1,13),(0,5),(5,20),(4,19),(10,0),(15,24),(31,5)], 3)

print(outptu1)
print(outptu1 == "16 4-19 U 13-6 16-6 1-9 7-18 12-22 10-20 29-5 24-21 4-21 3-20 11-14 25-16 23-23 7-8 1-16 10-21")

#### 3 ####

print("EXAMPLE 3")
print("INPUT")
print("8\n\
1 1\n\
1 6\n\
8 7\n\
3 6\n\
6 5\n\
6 6\n\
8 2\n\
5\n\
2 3\n\
6 8\n\
6 6\n\
1 3\n\
10 8\n\
3\n")

print("EXPECTED OUTPUT: ")
print("3 1-3 R 8-7 6-5 6-6")
print("RECEIVED OUTPUT:")
outptu1 = Avengers().destroyed_planets(
        [(1,1),(1,6),(8,7),(3,7),(6,5),(6,6),(8,2)],
      [(2,3),(6,8),(6,6),(1,3),(10,8)], 3)

print(outptu1)
print(outptu1 == "3 1-3 R 8-7 6-5 6-6")
print()

print("EXAMPLE 4")
print("INPUT")
print("8\n\
1 1\n\
1 7\n\
8 7\n\
3 8\n\
6 7\n\
2 7\n\
8 2\n\
5\n\
2 3\n\
7 8\n\
6 6\n\
1 3\n\
10 8\n\
3\n")

print("EXPECTED OUTPUT: ")
print("2 8-7 6-7")
print("RECEIVED OUTPUT:")
outptu1 = Avengers().destroyed_planets(
        [(1,1),(1,7),(8,7),(3,8),(6,7),(2,7),(8,2)],
      [(2,3),(7,8),(6,6),(1,3),(10,8)], 3)

print(outptu1)
print(outptu1 == "2 8-7 6-7")
