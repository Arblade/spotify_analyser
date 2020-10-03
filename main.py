from matplotlib import pyplot as plt
import numpy as np
from connect import *

def main(res):
    sections = res['sections']

    list_tempo = []
    list_pitch=[]
    #confidence
    list_tempo_conf = [] 
    list_pitch_conf=[]

    ## display of categories

    for item in sections :
        for key, elem in item.items():
            print('# {} --------> {} \n'.format(key,elem))
        list_tempo.append([item['start'],item['duration'],item['tempo']])
        list_tempo_conf.append(([item['start'],item['duration'],item['tempo_confidence']]))
        list_pitch.append([item['start'],item['duration'],item['key_confidence']])
        list_pitch_conf.append([item['start'],item['duration'],item['key']])

    ## display of tempo and notes



    print(list_tempo)

    x=(np.array(list_tempo)[:,1]+np.array(list_tempo)[:,0])/2
    # d=np.array(list_tempo)[:,1]
    tempos=np.array(list_tempo)[:,2]
    tempos_conf=np.array(list_tempo_conf)[:,2]
    notes = np.array(list_pitch)[:,2]
    notes_conf = np.array(list_pitch_conf)[:,2]

    print('--> La liste y ',tempos)
    print('--> La liste x ',x)

    plt.subplot(221)
    plt.title("Tempo en fonction du temps")
    plt.xlabel('temps')
    plt.ylabel('tempo')
    plt.axis([np.min(x),np.max(x) ,np.min(tempos),np.max(tempos)])
    plt.plot(x,tempos)

    plt.subplot(223)
    plt.title("Confidence tempo en fonction du temps")
    plt.xlabel('temps')
    plt.ylabel('tempo')
    plt.axis([np.min(x),np.max(x) ,np.min(tempos_conf),np.max(tempos_conf)])
    plt.plot(x,tempos_conf,'r')

    plt.subplot(222)
    plt.title('Pitch en focntion du temps')
    plt.xlabel('temps')
    plt.ylabel('picth')
    plt.plot(x,notes)

    plt.subplot(224)
    plt.plot(x,notes_conf,'r')
    plt.title('Confidence pitch en focntion du temps')
    plt.xlabel('temps')
    plt.ylabel('picth')

    plt.show()

if __name__=="__main__":
    # Rentrez le lien, ID ou track link de votre musique ici :
    song_id='https://open.spotify.com/track/2VN7uPrbryJ7nE2MXX3f9a?si=6WnU8vteSv-emrSCidFeYg'
    ## Connexion
    (client_id,client_secret) = get_info()
    con=connexion(client_id,client_secret)
    ## Obtention des résultats
    res=get_results(con,song_id)
    ## Lancement du main
    main(res)