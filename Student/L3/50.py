songs = ["_", "_", "_"]

def show_player():
    print("Плеєр:", " ".join(songs))

def get_song_num():
    num = int(input("Введіть номер пісні: "))
    if num == 0:
        exit()
    else:
        action = int(input("1 — запустити, 2 — зупинити:"))
        if action == 1:
            if songs[num-1] == '▶️':
                print("пісня вже грає")
            else:
                print("запустити")
                if '▶️' in songs:
                    index = songs.index('▶️')
                    songs[index] = "_"
                songs[num-1] = '▶️'
                


        else:
            if songs[num-1] == '_':
                print("Пісня вже зупинена")
            else:
                songs[num-1] = '_'
                print("зупинено")
                


while True:
    show_player()
    get_song_num()

        



