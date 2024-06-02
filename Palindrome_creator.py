def make_pali(text):
    #If the text is a palindrome then it'll return the text
    if text==text[::-1]:
        return text
    #Check for every single combination of palindromic letters
    for letters in range(0,len(text)):
        possibleans=text[0:letters]+text[::-1]
      #If the palindrome is equal to the text when spelt backwards
      #then it should be returned
        if possibleans==text[::-1]:
            return text+possibleans[1:]
