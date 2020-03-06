school_all = [{'school_class':'4a', 'scores':[3, 4, 5, 6, 7, 8]},
{'school_class': '4b', 'scores': [1, 1, 1, 1, 2]},
{'school_class': '5a', 'scores': [5, 5, 3, 5, 5, 4, 5, 5,5]}
]

kol_vo_ocenok = 0
kol_vo_vschool = 0
school_sum = 0
for a in range(3):
    klass_sum = 0
    for summa in school_all[a]['scores']:
        klass_sum += summa
    kol_vo_ocenok+=len(school_all[a]['scores'])
    kol_vo_vschool=kol_vo_vschool+len(school_all[a]['scores'])
    school_sum += klass_sum
    print(klass_sum)
    print(str(school_all[a]['school_class']) + ' : ' + str(klass_sum/len(school_all[a]['scores'])))
print(school_sum / kol_vo_vschool)
print ()



