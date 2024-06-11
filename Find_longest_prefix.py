def longestCommonPrefix(self, strs):
        #Get the first word as the valid prefix
        valid_pref=strs[0]
        #Move on to the next words
        for word in strs[1:]:
            #If word doesn't have a valid prefix then reduce prefix word by one
            while word[:len(valid_pref)]!=valid_pref:
                valid_pref=valid_pref[:-1]
        return valid_pref
