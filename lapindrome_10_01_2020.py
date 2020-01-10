# Python3 script to check if the string is Lapindromes or Not.

class CheckLapindrome():
    """ check multiple strings weither Lapindromes or Not.

    """
    def __init__(self):

        self.max_char = 26

    def checkLapindromeString(self, string): 
        """ checking string  Lapindromes or Not.

            Arguments :
                string : contain string values
            
            Return :
                Yes Lapindromes or NO Lapindromes

        """
        # Counter array inisialized with 0 
        count = [0] * self.max_char 
        # Length of the string 
        n = len(string) 
        if n == 1: 
            return true 
        # Traverse till the middle 
        # element is reached 
        i = 0; 
        j = n-1
        
        while i < j: 
            # First half 
            count[ord(string[i]) - ord('a')] += 1
            # Second half 
            count[ord(string[j])-ord('a')] -= 1

            i += 1; 
            j -= 1
        # Checking if values are 
        # different, set flag to 1 
        for i in range(self.max_char): 
            if count[i] != 0: 
                return False

        return True

if __name__ == "__main__":
    # creating instance of CheckLapindrome classgithub
    check_lapindrome = CheckLapindrome()

    #Input strings
    string_inputs = ['gaga', 'abcde', 'rotor', 'xyzxy', 'abbaab', 'ababc']
    # outputs
    for string in string_inputs: 
        print("Yes" if \
                check_lapindrome.checkLapindromeString(string) else "No") 



