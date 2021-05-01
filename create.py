import random
names = ['deathnote.txt', 'aot.txt', 'one_piece.txt', 
	'dragon_ball.txt', 'hunter_x_hunter.txt', 'kakegurui.txt', 
	'19_days.txt', 'banana_fish.txt', '¯\_(ツ)_/¯.txt', 
	'(▀̿Ĺ̯▀̿ ̿) .txt']

  
n = random.randint(0,len(names)-1)
with open(names[n], 'a+') as ff:
    pass


def file_work(names):
  for item in names:
    try:
        address='D:/Profiles/Admn/Desktop/'+item
        with open(address,'r+')as f:
            f=f.write('Elnura')
        print()
        print(f'Ваше имя записано в файл {item}')
    except OSError:
        print()
        print(f"{item} файла не существует")


file_work(names)
