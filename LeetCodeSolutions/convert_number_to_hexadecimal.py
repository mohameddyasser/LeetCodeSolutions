class Solution(object):
    def toHex(self, num):
        if num >= 0:
            converted_to_hex = format(num, 'x')
            return converted_to_hex
        else:
           converted_to_hex = '{:X}'.format(num & (2**32-1))
           return converted_to_hex.lower()

