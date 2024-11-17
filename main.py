import requests
import json
import numpy as np

from auth import Auth

base_url = 'https://api.spotify.com/v1/'

auth = Auth()
#auth.generate_token()    # use it only for the first time
token = auth.get_token()

headers = {
    'Authorization': f'Bearer {token}',
    "Accept": "application/json"
}

class artistas():
    lista_artistas=[]
    lista_generos=[]
    endpoint= 'me/top/artists'

    params = {
        'limit':10,
        'time_range':'long_term'
    }

    response = requests.get(base_url+endpoint, headers=headers, params=params)
    info_artistas=(response.json()['items'])
    for artista in info_artistas:
        lista_artistas.append(artista['name'])
        if artista['genres'][0] not in lista_generos:
            lista_generos.append(artista['genres'][0])
    
    #with open('resultados_actividad2.json','w') as file_top_artistas:
       # json.dump({'Top 10 artistas mas escuchados por el usuario':lista_artistas,'Top 5 generos favoritos del usuario':lista_generos[:5]},file_top_artistas,indent=2)
    print('Top 10 artistas:',lista_artistas,'Top 5 generos:',lista_generos)


class top_canciones():
    endpoint=('me/top/tracks')
    canciones=[]
    artistas=[]

    params={
        'limit':10,
        'time_range':'long_term'
    }

    response=requests.get(base_url+endpoint,headers=headers,params=params)
    info_tracks=(response.json()['items'])
    for cancion in info_tracks:
        canciones.append(cancion['name'])
        artistas.append(cancion['album']['artists'][0]['name'])

    canciones_artistas=dict(zip(canciones,artistas))

    #with open('resultados_actividad2.json','a') as file_top_canciones:
        #json.dump({'Top 10 canciones mas escuchadas por el usuario':canciones_artistas},file_top_canciones,indent=2)
    print('top canciones:',canciones_artistas)


class playlist():
    endpoint='playlists/37i9dQZF1DWWGFQLoP9qlv'
    response=requests.get(base_url+endpoint,headers=headers)

    portada=response.json()['images'][0]['url']
    imagen=requests.get(portada).content
    with open('portada_playlist.jpg','wb') as file:
        file.write(imagen)

    seguidores=response.json()['followers']['total']

    #with open('resultados_actividad2.json','a') as file_followers:
        #json.dump({'Followers_playlist':seguidores},file_followers,indent=2)
    print('Followers:',seguidores)

class features():
    endpoint='playlists/37i9dQZF1DWWGFQLoP9qlv/tracks'
    response=requests.get(base_url+endpoint,headers=headers)

    track_ids=[]
    
    info_id=(response.json()['items'])
    for track in info_id:
        track_ids.append('audio-features/'+track['track']['id'])

    tempo=[]
    acousticness=[]
    danceability=[]
    energy=[]
    instrumentalness=[]
    liveness=[]
    loudness=[]
    valence=[]

    for id in track_ids:
        response=requests.get(base_url+id,headers=headers)
        info_track=response.json()
        tempo.append(info_track['tempo'])
        acousticness.append(info_track['acousticness'])
        danceability.append(info_track['danceability'])
        energy.append(info_track['energy'])
        instrumentalness.append(info_track['instrumentalness'])
        liveness.append(info_track['liveness'])
        loudness.append(info_track['loudness'])
        valence.append(info_track['valence'])

    #with open('resultados_actividad2.json','a') as file_parametros_playlist:
        #json.dump ({'Parametros':{
            #'Valor medio de tempo':np.mean(tempo),
            #'Valor medio de acousticness':np.mean(acousticness),
            #'Valor medio de danceability':np.mean(danceability),
            #'Valor medio de energy':np.mean(energy),
            #'Valor medio de instrumentalness':np.mean(instrumentalness),
            #'Valor medio de liveness':np.mean(liveness),
            #'Valor medio de loudness':np.mean(loudness),
            #'Valor medio de valence':np.mean(valence)}},file_parametros_playlist,indent=2)
        
    print({'Parametros':{
            'Valor medio de tempo':np.mean(tempo),
            'Valor medio de acousticness':np.mean(acousticness),
            'Valor medio de danceability':np.mean(danceability),
            'Valor medio de energy':np.mean(energy),
            'Valor medio de instrumentalness':np.mean(instrumentalness),
            'Valor medio de liveness':np.mean(liveness),
            'Valor medio de loudness':np.mean(loudness),
            'Valor medio de valence':np.mean(valence)}})
    
   
 

        

    


        






