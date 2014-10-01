import sys

from FilmsTropesParser import FilmsTropesParser

def main(argv):

    if len(sys.argv) < 3:

        print "Python Tropes Parser Usage: "
        print sys.argv[0], '\'<Path of input directory> <Path of output directory>\''
        sys.exit()

    filmsParser = FilmsTropesParser(sys.argv[1])
    filmsOutput = filmsParser.parseFilms()

    outputFile = open(sys.argv[2], 'w')
    outputFile.write(filmsOutput)
    outputFile.close()

if __name__ == '__main__':
    main(sys.argv)
