## Функция, которая использует cook_book
def get_shop_list_by_dishes(dishes, person_count):
    buy_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            quantity = ingridient['quantity'] * person_count
            if ingridient['ingridient_name'] not in buy_list:
                buy_list[f'{ingridient['ingridient_name']}'] = {'quantity': quantity, 'measure': ingridient['measure']}
            else:
                buy_list[f'{ingridient['ingridient_name']}']['quantity'] += quantity
    return buy_list


## Функция, которая НЕ использует cook_book
def get_shop_list_by_dishes_v2(dishes, person_count):
    buy_list = {}
    with open('recipes.txt', encoding='UTF-8-sig') as f:
        for line in f:
            name_dish = line.strip()
            count = int(f.readline())
            if name_dish in dishes:
                for h in range (0, count):
                    ingridient = f.readline()
                    name, quantity, measure = ingridient.split('|')
                    if name not in buy_list:
                        buy_list[f'{name}'] = {'quantity': int(quantity) * person_count, 'measure': measure.strip().strip()}
                    else:
                        buy_list[f'{name}']['quantity'] += int(quantity) * person_count
                ingridient = f.readline()
            else:
                for h in range (0, count + 1):
                    f.readline()
    return buy_list


cook_book = {}
with open('recipes.txt', encoding = 'UTF-8-sig') as f:
    for line in f:
        name_dish = line.strip()
        count = int(f.readline())
        cook_book[f'{name_dish}'] = []
        for h in range (0, count):
            ingridient = f.readline()
            name, quantity, measure = ingridient.split('|')
            cook_book[f'{name_dish}'].append({'ingridient_name': name, 'quantity': int(quantity), 'measure': measure.strip()})
        ingridient = f.readline()
    f.close()
        
print(cook_book, '\n\n\n\n')
print(get_shop_list_by_dishes(['Омлет', "Фахитос"], 3), '\n\n\n\n')
print(get_shop_list_by_dishes_v2(['Омлет', "Фахитос"], 3))
     
            



