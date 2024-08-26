"""Linear search aka Brute force method is basically searching 
    through the list linearly and terminate when desired output
    is found."""
#Linear search- Values(Number that we want), numbers(List of numbers)
def search(value,numbers):
  #Iterate through every single element of that list.
    for i, num in enumerate(numbers):
        if value == num:
            return i
          #Return none if the value is not found in the list of numbers
    return None 

"""More efficient than linear search, basically breaking the list in half
   then comparing the middle point to the value to check if it is larger or smaller.
   Then reduce the list size by changing the end """
#Binary search
array=[1,15,26,8,29,18,28,3]


def Easier_binary_search(search,arrays):
    #sort the list out
    new_array=sorted(arrays)
    #set starting and ending point
    start=0
    end=len(new_array)-1
    middle=0

    #If start and end is not the middle value
    while(start<end):
        #Always adjust middle value
        middle=start+(end-start)//2
        #If middle value is less than desired value shift right
        if(new_array[middle]<search):
            start=middle+1
       #If middle value is more than desired value shift left
        if(new_array[middle]>search):
            end=middle-1
        if(new_array[middle]==search):
            print(new_array)
            return middle
    
