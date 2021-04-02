import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from random import randrange
from read_pics import get_pics_from_file
import pandas as pd


def get_na(file, n):
    pics, info = get_pics_from_file("Hackaton/data/" + file)
    X = []
    for i in range (0, n):
        a = [j for j in pics[i]]
        X.append(a)
    
    na = np.array(X)
    return na

if __name__ == "__main__":
    na50 = get_na("pics_NOKEY.bin", 7000)

    for k in range (2, 5):
        kmean = KMeans(n_clusters=k, random_state=randrange(200))
        pred50 = kmean.fit_predict(na50)
        cc = np.transpose(kmean.cluster_centers_)
        print(cc)
        plt.subplot(2,2,k)
        plt.scatter(na50[:, 0], na50[:, 1], c =pred50)
        plt.scatter(cc[0], cc[1], c='red')
        plt.xlabel("Prediction pour k = {0}".format(k))

    # k = 4
    # kmean = KMeans(n_clusters=k, random_state=randrange(200))
    # pred50 = kmean.fit_predict(na50)
    # cc = np.transpose(kmean.cluster_centers_)
    # print(cc)
    # plt.scatter(na50[:, 0], na50[:, 1], c =pred50)
    # plt.scatter(cc[0], cc[1], c='red')
    # plt.xlabel("Prediction pour k = {0}".format(k))

    plt.show()