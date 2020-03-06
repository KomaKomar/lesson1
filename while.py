vopr = {
    'Как ты?': 'Норм',
    'Че ты':'Кайфую'
}


while True:
    try:
        a=input()
        if a in vopr:
            print(vopr[a])
        else:
            print('выйди и спроси нормально')
    except (KeyboardInterrupt):
        print("Чао")
        break


