class Calculator:
    def __init__(self, number, start_base, final_base):
        self.number = number
        self.start_base = start_base
        self.final_base = final_base

    def any_to_tenth_integer(self):
        dictionary = {value: key for (key, value) in (dict(enumerate(list('0123456789abcdefghijklmnopqrstuvwxyz')))).items()}
        a = [dictionary[i.lower()] for i in list(str(self.number))][::-1]
        rez = 0
        for i, value in enumerate(a):
            rez += value * self.start_base ** i

        return rez


    def any_to_tenth_float(self):
        dictionary = {value: key for (key, value) in (dict(enumerate(list('0123456789abcdefghijklmnopqrstuvwxyz')))).items()}
        first_part = first_part = [i.lower() for i in list((str(self.number).replace(',', '*').replace('.', '*').split('*'))[0])][::-1]
        second_part = [i.lower() for i in list((str(self.number).replace(',', '*').replace('.', '*').split('*'))[1])]
        rez_fp, rez_sp, for_sp = 0, 0, -1
        for i, value in enumerate(first_part): rez_fp += dictionary[str(value)] * self.start_base ** i
        for i in second_part:
            rez_sp += dictionary[str(i)] * self.start_base ** for_sp
            for_sp -= 1
    
        return rez_fp + rez_sp
    
    def tenth_to_any_int(self):
        digits = '0123456789abcdefghijklmnopqrstuvwxyz'
        if self.final_base > len(digits): return None
        result = ''
        while self.number > 0:
            result = digits[self.number % self.final_base] + result
            self.number //= self.final_base

        print(result.upper())
        return result.upper()
    
    
number = Calculator('A10b,a', 16, 10)

print(number.any_to_tenth_float())
