import string
import random

class Utils:
    @staticmethod
    async def genString(stringLength):
        try:
            letters = string.ascii_letters + string.digits
            return ''.join(random.choice(letters) for i in range(stringLength))
        except Exception as error:
            print(error)

    @staticmethod		    
    async def digitString(stringLength):
        try:
            digit = string.digits
            return ''.join((random.choice(digit) for i in range(stringLength)))    
        except Exception as error:
            print(error)	
