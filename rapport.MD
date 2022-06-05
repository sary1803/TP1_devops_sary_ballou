# TP1 DEVOPS
## Créer un wrapper qui retourne la météo d'un lieu donné avec sa latitude et sa longitude
Le wrapper sera codé en python
        Création d'une fonction pour récupérer les variables d'environnement

```
def get_env():
    env= os.environ
    lattitude= env['LAT']
    longitude=env['LONG']
    api_key=env['API_KEY']

    return lattitude,longitude,api_key
```
        Création d'une fonction qui retourne la météo en fonction des variables d'environnements
        mis en paramètres
```
def meteo(lat,lon,api_key):
    url = "http://api.openweathermap.org/data/2.5/weather?"
    url = url + "lat=" + lat + "&lon=" + lon + "&appid=" + api_key
    response = requests.get(url)
    data = json.loads(response.text)

    return data
```
    Ecriture d'un main pour executer les fonctions
```
if __name__=="__main__":
    lat,lon,api_key= get_env()
    Meteo=meteo(lat,lon,api_key)
    print(Meteo)

```

## Packager son code dans une image Docker
Modification du ADD EN COPY  et Ajout du --no-cache-dir et de la version de requests pour supprimer les lints errors

```
FROM python:latest
COPY . /app/
WORKDIR /app
RUN pip install --no-cache-dir requests==2.25.1

CMD ["python","meteo.py"]


```
## Mettre à disposition son image sur DockerHub
J'ai des difficultés à mettre l'image sur Dockerhub, le terminal m'indique que cela a été fait mais je ne retrouves pas l'image sur docker hub après plusieurs essais.
## Mettre à disposition son code dans un repository Github
https://github.com/sary1803/TP1_devops_sary_ballou