def fibonacci(n):
    """Add the previous number and the previous 2 number to form
    a new number"""
    #Backwards addition until it hits base case
    """E.g. fibonacci(4)
    4- 3+2=5
    3-2+1=3
    2-1+1=2
    1-1

    1+1=2+1=3+2=5
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    
    return fibonacci(n-1)+fibonacci(n-2)
