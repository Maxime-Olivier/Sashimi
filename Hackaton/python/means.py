from read_pics import get_pics_from_file
import matplotlib.pyplot as plt



def get_average(file):
    average_plot = []
    pics, info = get_pics_from_file("Hackaton/data/" + file)
    for i in range(0, len(pics[0])): #on boucle autant de fois qu'il y a de valeurs
        value = 0
        for j in range(0, len(pics)): #on boucle sur chacun des échantillon pour recupérer sa ieme valeur
            value += pics[j][i]
        average_plot.append(value / len(pics))
    
    return average_plot




if __name__ == "__main__":


    pics_nokey, info = get_pics_from_file("Hackaton/data/pics_NOKEY.bin")
    plt.figure(1)

    avg_nokey = get_average("pics_NOKEY.bin")
    plt.plot(range(1,info["nb_pics"]+1), avg_nokey, 'ko')
    plt.xlabel('numéro de pic')
    plt.ylabel('valeur du pic')
    plt.title('average_nokey')
    plt.ylim(0, 1.5)
    plt.grid(b=True, which='both')


    for k in range (1, 10):
        key = chr(ord('A') - 1 + k)
        
        plt.subplot(3,3,k)
        average_plot = get_average("pics_" + key  + ".bin")
        plt.plot(range(1,info["nb_pics"]+1), avg_nokey, 'ko', color = 'red')
        plt.plot(range(1,info["nb_pics"]+1), average_plot, 'ko', color = 'b')
        plt.plot(range(1,info["nb_pics"]+1), get_average("pics_LOGINMDP.bin"), 'ko', color = 'g')

        print(key , average_plot)
        plt.xlabel('numéro de pic')
        plt.ylabel('valeur du pic')
        plt.title(key)
        plt.ylim(0, 1.5)
        plt.grid(b=True, which='both')
    
    plt.show()

    # plt.figure(2)
    # for k in range (1, 10):
    #     key = chr(ord('0') - 1 + k)
    #     plt.subplot(3,3,k)
    #     average_plot = get_average("pics_" + key  + ".bin")
    #     plt.plot(range(1,info["nb_pics"]+1), avg_nokey, 'ko', color = 'red')
    #     plt.plot(range(1,info["nb_pics"]+1), average_plot, 'ko')
    #     plt.plot(range(1,info["nb_pics"]+1), get_average("pics_LOGINMDP.bin"), 'ko', color = 'g')
    #     print(key , average_plot)
    #     plt.xlabel('numéro de pic')
    #     plt.ylabel('valeur du pic')
    #     plt.title(key)
    #     plt.ylim(0, 1.5)
    #     plt.grid(b=True, which='both')

    #plt.show()