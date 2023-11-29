class Dz():
    def __init__(self,s):
        self.s = s

    def reshenie(self):
        num_even = []
        vowels = 'aeyuio'
        list_vow =[]
        list_cons =[]
        count_vow = 0
        count_cons = 0
        self.s = str(self.s)
        if self.s.isdigit():
            for i in self.s:
                if int(i) % 2 == 0:
                    num_even.append(i)
                else:
                    continue
            summ = 0
            for i in num_even:
                summ += int(i)
            return print(summ * len(self.s))
        if self.s.isalpha():
            for i in self.s:
                if i in vowels:
                    count_vow += 1
                    list_vow.append(i)
                else:
                    count_cons += 1
                    list_cons.append(i)
            multp_ch =count_cons * count_vow
            if multp_ch <= len(self.s):
                return print(list_vow)
            else:
                return print(list_cons)





