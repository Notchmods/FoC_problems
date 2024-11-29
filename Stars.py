"""Printing the amount of stars in pyramid shape
e.g. 
Rows=3
    *
   ***
  *****
Strategy- 
Determining the spacing by count the amount of rows there are and subtract it by
the current row
  """
a=int(input("How many rows of triangles "))

Oddifier=0 #Make the number of stars printed odd
#a- Number of rows
#i- Initial loop(row by row)
#j,k- How many time it is printed in the row.

for i in range(a):#No. of rows to print
    #Decrease space printed as more stars are printed
    for j in range(a-i+1):
        print(" ", end="")
    #print stars
    for k in range(((i+Oddifier)-1)):
        print("*",end="")
    print("\n")
    Oddifier+=1
