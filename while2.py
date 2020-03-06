#def discounted(price, discount, max_discount=20):
while True:
    try:
        price = abs(float(input()))
        discount = abs(float(input()))
        max_discount = abs(float(input()))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
             print('цена остается таже: ' + str(price))
        else:
             print('цена со скидкой: ' + str(price - (price * discount / 100)) +  '\nразмер скидки = ' + str(price * discount / 100))
    except (ValueError):
        print('Введите число')
    except (KeyboardInterrupt):
        print('Забегай, еще покодим') 
        break
        