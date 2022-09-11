import os
import pandas as pd
import requests
import urllib.request

df = pd.read_csv('imgspin1.csv', delimiter=';')
print(df.iloc[1][5])#[kolumny][wiersze]

print(len(df.iloc[1]))

zmienna_kod = df.iloc[0][0][df.iloc[0][0].find('/jpeg/')+6:df.iloc[0][0].rfind('_R0')]#to do nazwy folderu
print(zmienna_kod)
#zmienna_r = df.iloc[0][0][df.iloc[0][0].find('_R0')+3:df.iloc[0][0].rfind('_C')]
#print(zmienna_r)
zmienna_c = df.iloc[0][0][df.iloc[0][0].find('_C')+2:df.iloc[0][0].rfind('.jpg')]
print(zmienna_c)
print("size: ", df.size)
iterate_size = df.size

directory = zmienna_kod
parent_dir = r"C:\Users\Filip Kordusiak\PycharmProjects\pythonProject\sortowanie\spin"
path = os.path.join(parent_dir, directory)
#os.mkdir(path)
iterate = 0
for i in range(0, len(df)): #↓ to są kolumny
    # tutaj nastapi stworzenie folderu z podziałem na 1 oraz 2
    dir_name = df.iloc[i][0][df.iloc[i][0].find('/jpeg/') + 6:df.iloc[i][0].rfind('_R0')]  # to do nazwy folderu
    print("fff", dir_name)
    directory = dir_name
    parent_dir = r"C:\Users\Filip Kordusiak\PycharmProjects\pythonProject\sortowanie\spin"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    parent_dir = r"C:\Users\Filip Kordusiak\PycharmProjects\pythonProject\sortowanie\spin\{0}".format(dir_name)
    path = os.path.join(parent_dir, '1')
    os.mkdir(path)
    parent_dir = r"C:\Users\Filip Kordusiak\PycharmProjects\pythonProject\sortowanie\spin\{0}".format(dir_name)
    path = os.path.join(parent_dir, '2')
    os.mkdir(path)

    for ii in range(0, len(df.iloc[i])): #↓ a to są wiersze
        zmienna_r = 'nan'
        print((iterate/iterate_size)*100, " %")
        iterate += 1
        try:
            zmienna_r = df.iloc[i][ii][df.iloc[i][ii].find('_R0') + 3:df.iloc[i][ii].rfind('_C')]
        except:
            pass
        if zmienna_r == '1':

            parent_dir_1 = r"C:\Users\Filip Kordusiak\PycharmProjects\pythonProject\sortowanie\spin\1"
            imgURL = f"{df.iloc[i][ii]}"
            print("img url", imgURL)
            if not imgURL == 'nan':
                zmienna_cc = df.iloc[i][ii][df.iloc[i][ii].find('_C') + 2:df.iloc[i][ii].rfind('.jpg')]
                urllib.request.urlretrieve(imgURL, "C:/Users/Filip Kordusiak/PycharmProjects/pythonProject/sortowanie/spin/{0}/1/".format(dir_name) + zmienna_cc + ".jpg")
            else:
                break

        elif zmienna_r == '2':
            parent_dir_1 = r"C:\Users\Filip Kordusiak\PycharmProjects\pythonProject\sortowanie\spin\1"
            imgURL = f"{df.iloc[i][ii]}"
            print("img url", imgURL)
            if not imgURL == 'nan':
                zmienna_cc = df.iloc[i][ii][df.iloc[i][ii].find('_C') + 2:df.iloc[i][ii].rfind('.jpg')]
                urllib.request.urlretrieve(imgURL, "C:/Users/Filip Kordusiak/PycharmProjects/pythonProject/sortowanie/spin/{0}/2/".format(dir_name) + zmienna_cc + ".jpg")
            else:
                break
        else:
            print("url = NaN")
