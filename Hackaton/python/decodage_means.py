import matplotlib.pyplot as plt
from read_pics import get_pics_from_file
import os
import operator
import random



'''
renvoie la courbe moyenne de toutes les trames d'un symbole
input: nom du fichier (string)
'''
def get_average(file):
    average_plot = []
    pics, _ = get_pics_from_file("Hackaton/data/" + file)
    for i in range(len(pics[0])): #on boucle autant de fois qu'il y a de valeurs
        value = 0
        for j in range(len(pics)): #on boucle sur chacun des échantillon pour recupérer sa ieme valeur
            value += pics[j][i]
        average_plot.append(value / len(pics))
    
    return average_plot


'''
renvoie une liste contenant le premier élément de chaque tuple de la liste de départ
input: liste de tuple à nettoyer
'''
def clean_res(l):
    res = []
    for a, _ in l:
        res.append(a)

    return res


'''
renvoie un tableau à 2 dimensions contenant toutes les moyennes de tous les symboles
input:
'''
def get_all_files():
    data = []  
    for file in os.listdir("Hackaton/data/"):
        if file != "pics_LOGINMDP.bin":
            avg = get_average(file)
            name = file[5:len(file) - 4]
            data.append((name,avg))
 
    return data


'''
renvoie pour chaque trame du fichier "LOGINMDP" le caractère qui se rapproche le plus de celle ci
input: tableau à 2 dimensions 
'''
def summeans_match(avgs):
    pics_loginmdp, _ = get_pics_from_file("Hackaton/data/pics_LOGINMDP.bin")
    res = []
    for trame in range(len(pics_loginmdp)):
        diffs = []
        for name, key in avgs:
            diff = 0
            for i in range(len(pics_loginmdp[trame])):
                diff += abs(key[i] - pics_loginmdp[trame][i]) /17
            
            diffs.append((name,diff))
            diff = 0

        res.append(min(diffs, key = lambda t: t[1]))
        
    return res


'''
renvoie un tableau d'occurrences
input: tableau de tuple 
'''
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


'''
renvoie un tableau regroupant les caractères ayant des variations similaires
input: 
'''
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
     

'''
transforme le tableau en les rassemblant par groupes de variations proches
input: un tableau à une dimension
'''
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
            
            
'''
supprime toutes les listes de longueur inférieure à 10 du tableau
input: tableau à 1 dimension
'''
def clean_short_list(arr):
    res = []
    for i in arr:
        if len(i) > 10:
            res.append(i)

    return res


'''
renvoie les 3 caractères ayant le plus d'occurences
input: tableau de tuple
'''
def key_rank_with_block(arr):
    res = []
    for bloc in arr:
        nb_occ = count_occ(bloc)
        nb_occ.sort(key=lambda tup: tup[1], reverse=True)
        res.append(nb_occ[:3])

    return res


'''
renvoie une liste de tableaux contenant les caractères séparés à l'aide des symboles "NOKEY"
input: tableau à une dimension
'''
def key_rank_nokey(arr):
    res = []
    length = len(arr)
    i = 0
    bloc = []
    count = 0
    for i in range(length):

        if arr[i] == 'NOKEY':
            count += 1
        else :
            bloc.append(arr[i])
            count = 0
        
        if (count > 3):
            res.append(bloc)
            bloc = []

    res = clean_short_list(res)
    res = key_rank_with_block(res)

    return res


if __name__ == "__main__":

    data = summeans_match(get_all_files())
    final = clean_res(data)
    unite_letter(final)
    res = key_rank_nokey(final)

    print("~~~~~~~~RESULTATS~~~~~~~~") 
    print(res)

    k = 1    
    for elm in res:
        plt.subplot(3, 5, k)
        res_letter = [i for i, _ in elm]
        res_num = [j for _,  j in elm]
        plt.bar(res_letter, res_num)
        k += 1

    mng = plt.get_current_fig_manager()
    mng.window.state("zoomed")

    plt.show()
