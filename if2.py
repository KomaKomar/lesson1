def dva_slova(a, b):
    if type(a)==str and type(b)==str:
        if a == b:
            return'1'
        elif len(a) < len(b):
            if  b == 'learn':
                return'3' 
            return'2'
        return'0'


a = input()
b = input()
print(dva_slova(a,b))