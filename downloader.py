from pytube import YouTube
from pytube.cli import on_progress
import os


def main():
    path = input('Chemin du repertoire pour stocker la vidéo: ')
    url = input("Url de la vidéo à télécharger: ")
    video = YouTube(url, on_progress_callback=on_progress)

    quality = input("1- Qualité par défaut\n" +
                    "2- Faible résolution\n" +
                    "3- Haute résolution\n")

    try:
        if quality == 1:
            video = video.streams.filter(progressive=True, file_extension='mp4').first()
        elif quality == 2:
            video = video.streams.filter(progressive=True, file_extension='mp4').get_lowest_resolution()
        else:
            video = video.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()


        try:
            if video is not None:
                print("Téléchargement...")
                name_file = video.title + ".mp4"
                if os.path.exists(path + "/" + name_file + '.mp4'):
                    return 'Ce nom de fichier est déjà utilisé.'
        
                video.download(path, name_file)
                print(str(round(video.filesize/(1024*1024))) + 'MB  ')
                show_dir = os.system("open %s" % path)
                print(show_dir)
                
            return 'Fichier téléchargé.'
        except:
            return "Erreur de téléchargement de la vidéo de l'url: " + str(url)
    except:
        return "Erreur de connexion"


def simple():
    video = input("Url de la video: ")
    video = YouTube(video, on_progress_callback=on_progress)

    file_path = input("Repertoire: ")

    try:
        stream = video.streams.filter(progressive=True, file_extension='mp4').first()

        if stream is not None:
            file_name = stream.title + '.mp4'
            stream.download(file_name, file_path + '/' + file_name)
            show_dir = os.system("open %s" % file_path)
            print(show_dir)
        
            return str(round(stream.filesize / (1024*1024))) + 'MB '

        return 'Fichier non créé. Erreur !'
    except:
        return 'Connexion perdue'


print(main())
