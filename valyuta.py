import sys

def val():
    print('Введіть курс Біткоина')
    bitok = float (sys.stdin.readline())
    if bitok <=-1:
        print('введіть чісло більше або дорівнююче нулю')
    print ('Введіть курс евро')
    dol= float(sys.stdin.readline())
    if dol <= -1:
        print('Вводіть число більше або дорівнююче нулю')
    converted_bitok=float(bitok)
    converted_dol=float(dol)
    print(converted_bitok*converted_dol)
    
val()
