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
def B_search(value,numbers):
    #Define start and end points
    start=0
    end=(len(numbers)-1)
    #The list hasn't been iterated through
    while start<=end:
        #Break the list into half
        middle = start+(end-start)//2
        """Check if the middle number is smaller or larger
        than the desired value"""
        if numbers[middle]<value:
            #Increase the start size to the right of the middle list.
            start= middle+1
        elif numbers[middle]>value:
            #If larger then decrease the end size to the left of middle list.
             end=middle-1
        else:
            return middle
    #Return none when nothing is found
    return None
    
