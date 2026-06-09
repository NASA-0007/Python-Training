def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)//2):
            if(s[i].isalnum()==False):
                continue
            for j in range(-1,-(len(s))):
                print(s[j])
                if(s[j].isalnum()==False):
                    continue
                elif (s[i].lower())!=(s[j].lower()):
                    return False
        return True