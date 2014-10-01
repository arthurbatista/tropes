from TropesRegexParser import DBTropesParser
from film import Film
from films import Films

from os import listdir
from os.path import isfile, join
import json

class FilmsTropesParser():

    def __init__(self, filmsInputFolderPath):

        self.films = Films()
        self.tropesParser = DBTropesParser()
        self.filmsInputFolderPath = filmsInputFolderPath

    def parseFilms(self):

        for f in listdir(self.filmsInputFolderPath):
            filmFilePath = join(self.filmsInputFolderPath, f)

            if isfile(filmFilePath):

                #parse the film
                filmFile = open(filmFilePath, 'r')

                tropes = self.tropesParser.parseTropes(filmFile.read())
                filmName = f

                self.films.films.append(Film(filmName, tropes))

                filmFile.close()

        #transform the self.films object in a JSON
        return json.dumps(self.films, default=lambda o: o.__dict__)
