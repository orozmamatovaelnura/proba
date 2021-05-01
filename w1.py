example1 = {
	   'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15/2, False],
	   'fire': ['hot', 46, ['cha', 'ching'], 81.13],
	   'earth': ['solid', 100, (13, 31, 1), 90.01, {'b':'c'}]
	   }

elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']

def try_except_func(example1,elements):
  for item in elements:
    try:
      summ=0
      for st in example1[item]:
        try:
          summ+=st
        except:
          continue
      print(item,'-',summ)

    except:
      print(f'Ключа {item} не существует')


try_except_func(example1,elements)
