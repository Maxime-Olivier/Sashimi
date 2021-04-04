import matplotlib.pyplot as plt
from read_pics import get_pics_from_file
import os
import operator
import random


def get_average(file):
    average_plot = []
    pics, info = get_pics_from_file("Hackaton/data/" + file)
    for i in range(0, len(pics[0])): #on boucle autant de fois qu'il y a de valeurs
        value = 0
        for j in range(0, len(pics)): #on boucle sur chacun des échantillon pour recupérer sa ieme valeur
            value += pics[j][i]
        average_plot.append(value / len(pics))
    
    return average_plot


def clean_res(l):
    res = []
    for a, b in l:
        res.append(a)
    return res


def get_all_files():
    data = []  
    for file in os.listdir("Hackaton/data/"):
        if file != "pics_LOGINMDP.bin":
            avg = get_average(file)
            name = file[5:len(file) - 4]
            data.append((name,avg))
 
    return data


def summeans_match(avgs):
    pics_loginmdp, info = get_pics_from_file("Hackaton/data/pics_LOGINMDP.bin")
    res = []
    vrai_res = []
    for trame in range(0, len(pics_loginmdp)):
        diffs = []

        for name, key in avgs:
            diff = 0

            for i in range(0, len(pics_loginmdp[trame])):
                diff += abs(key[i] - pics_loginmdp[trame][i]) /17
            diffs.append((name,diff))
            diff = 0

        res.append(min(diffs, key = lambda t: t[1]))
        
    return res


def count_occ(arr):
    res = []
    for key in arr:
        found = False
        for i in range(len(res)):
            if res[i][0] == key:
                res[i] = (res[i][0],res[i][1] + 1)
                found = True
                break
        if found == False:
            res.append((key, 1))

    return res


def key_rank(n, arr):
    occ = []
    res = []
    for k in range(0, len(arr)):
        if k % n == 0 and k != 0:
            nb_occ = count_occ(occ)
            nb_occ.sort(key=lambda tup: tup[1], reverse=True)
            res.append(nb_occ[:3])
            occ = []
            nb_occ = []

        occ.append(arr[k])


    nb_occ = count_occ(occ)
    nb_occ.sort()
    res.append(nb_occ[:3])
    return res


def find_similar():
    data = get_all_files()
    res = []
    for name_compare, pics_compare in data:

        similar = []
        similar.append(name_compare)

        for name, pics in data:
            if (name == name_compare):
                continue
            diff = 0

            for i in range(0, len(pics)):
                diff += abs(pics_compare[i] - pics[i])
            
            if diff < 0.25:
                similar.append(name)

        res.append(similar)
    return res
     
    
def unite_letter(arr):
    for i in range(len(arr)):
        if (arr[i] in ['1', '2', '3', '4']):
            arr[i] = "1234"
        elif (arr[i] in ['5', '7', '8']):
            arr[i] = "578"
        elif (arr[i] in ['6', '9']):
            arr[i] = "69"
        elif (arr[i] in ['A', 'W', 'Q']):
            arr[i] = "AWQ"
        elif (arr[i] in ['B', 'H', 'U']):
            arr[i] = "BHU"
        elif (arr[i] in ['D', 'E']):
            arr[i] = "DE"
        elif (arr[i] in ['F', 'R']):
            arr[i] = "FR"
        elif (arr[i] in ['G', 'T', 'Y']):
            arr[i] = "GTY"
        elif (arr[i] in ['H', 'B', 'U']):
            arr[i] = "HBU"
        elif (arr[i] in ['M', 'P']):
            arr[i] = "MP"
        elif (arr[i] in ['X', 'Z']):
            arr[i] = "XZ"
        elif (arr[i] in ['SPACE', 'S']):
            arr[i] = "SPACE S"
            
            
def clean_short_list(arr):
    res = []
    for i in arr:
        if len(i) > 10:
            res.append(i)
    return res


def key_rank_with_block(arr):
    res = []
    for bloc in arr:
        nb_occ = count_occ(bloc)
        nb_occ.sort(key=lambda tup: tup[1], reverse=True)
        res.append(nb_occ[:3])
    return res


def key_rank_nokey(arr):
    res = []
    lenght = len(arr)
    i = 0
    bloc = []
    count = 0
    while i < lenght:

        if arr[i] == 'NOKEY':
            count += 1
        else :
            bloc.append(arr[i])
            count = 0
        
        if (count > 3):
            res.append(bloc)
            bloc = []

        i += 1

    res = clean_short_list(res)

    res = key_rank_with_block(res)

    return res


if __name__ == "__main__":

    data = summeans_match(get_all_files())
    final = clean_res(data)
    
    print("~~~~~~~~RESULTATS~~~~~~~~")    
    
    unite_letter(final)

    res = key_rank_nokey(final)
    
    '''
    print(len(final))

    res = key_rank(120, final)
    k = 1
    print(res)
    for elm in res:
        plt.subplot(6, 7, k)
        res_letter = [i for i, _ in elm]
        res_num = [j for _,  j in elm]
        plt.bar(res_letter, res_num)
        k += 1
    
    plt.show()
    '''
    res = find_similar()
    for x in res:
        print(x)
