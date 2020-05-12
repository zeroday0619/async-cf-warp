import string
import random

class Utils:
    @staticmethod
    async def genString(stringLength):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    
    @staticmethod
    async def digitString(stringLength):
        digits = string.digits
        return ''.join((random.choice(digits) for i in range(stringLength)))