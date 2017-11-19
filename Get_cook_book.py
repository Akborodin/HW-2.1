cook_book = dict()

def read_ingridient(file):
  ingridient = dict()
  try:
    lines = file.readline().split('|')
    ingridient["ingridient_name"] = lines[0].strip(" ")
    ingridient["quantity"] = int(lines[1].strip(" "))
    ingridient["measure"] = lines[2].strip()
    return ingridient
  except:
    print("Invalid ingridient format")
    return ingridient

def read_cook_book(filename):
  dish_list = {}

  with open (filename, 'r', encoding='utf-8-sig') as f:
    while True:
      dish_name = f.readline().lower().strip()
      if (dish_name.strip() == ''):
        break
      ingridient_count = int(f.readline())
      ingridient_list = []
      for i in range(0, ingridient_count):
        ingridient_list.append(read_ingridient(f))
      dish_list[dish_name] = ingridient_list
    
    print ('Текущий список блюд:', dish_list)
    return dish_list


def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

cook_book = read_cook_book('cook_book.txt')
create_shop_list()
