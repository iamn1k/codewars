class RomanNumerals:
    def to_roman(data):
        rom = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        str_data = str(data)
        str_data = str_data[::-1]
        num_digits = len(str_data)
        ans = ""
        rom_pointer = 0

        for place in range(num_digits):
            if str_data[place] in ["0", "1", "2", "3"]:
                ans = rom[rom_pointer] * int(str_data[place]) + ans
            elif str_data[place] in ["4"]:
                ans = rom[rom_pointer] + rom[rom_pointer + 1] + ans
            elif str_data[place] in ["5", "6", "7", "8"]:
                ans = rom[rom_pointer + 1] + rom[rom_pointer] * (int(str_data[place]) - 5) + ans
            elif str_data[place] in ["9"]:
                ans = rom[rom_pointer] + rom[rom_pointer + 2] + ans
            rom_pointer += 2
        return ans
    def from_roman(s):
        R = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = s[-1]
        res = R[prev]
        for cur in s[-2::-1]:
            if R[cur] >= R[prev]:
                res += R[cur]
            else:
                res -= R[cur]
            prev = cur
        return res