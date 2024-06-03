board=[[1,5,10,4],[8,9,7,12],[20,21,30,35]]  
"""Input:[[1,5,10,4],[8,9,7,12],[20,21,30,35]]  
  Output:[[1, 4, 5, 7], [8, 9, 10, 12], [20, 21, 30, 35]]"""
def sort_board(board):
    all_letters=[]
    current_board=[]
    new_board=[]
    #Get letters into a list
    for rows in board:
        for letters in rows:
            all_letters.append(letters)

    #Sort the list out
    for i,items in enumerate(sorted(all_letters)):
        #Assuming that each list within sublist is a similar size
        if len(current_board)<len(board[0]):
            current_board.append(items)
        else:
            #If it surpass the length of the sublist
            new_board.append(current_board)
            #Current list is cleared and items is added to new list
            current_board=[]
            current_board.append(items)

            #Solve problem where final sublist is appended.
        if i==(len(all_letters)-1):
            new_board.append(current_board)
            
    return new_board
