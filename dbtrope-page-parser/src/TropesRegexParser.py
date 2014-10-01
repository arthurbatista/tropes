import re
from tropes import Trope

class DBTropesParser():

    def parseTropes(self, text):

        self.initDataStructures()

        listOfTableLines = self.extractTableLines(text)

        self.parseTableLines(listOfTableLines)

        return self.tropesList

    def initDataStructures(self):

        self.tropesList = []
        self.initTempTropeDataStructures()

    def initTempTropeDataStructures(self):

        self.tropeTypeFound = False
        self.trope = Trope()

    def extractTableLines(self, text):

        return re.split('<tr([\s\S]+?)\\\n<\/tr>', text)

    def parseTableLines(self, listOfTableLines):

        for i in range(len(listOfTableLines)):

            tableLine = listOfTableLines[i]

            if self.isEmptyTableLine(tableLine):
                continue

            self.parseEachTableLine(tableLine)

    def isEmptyTableLine(self, tableLine):

        return not re.match('\s*\w+', tableLine)

    def parseEachTableLine(self, tableLine):

        isTypeTable = self.isTypeTable(tableLine)

        self.parseTableLine(isTypeTable, tableLine)

    def isTypeTable(self, tableLine):

        return re.search(
            '<div title=\'http\:\/\/www\.w3\.org\/1999\/02\/22-rdf-syntax-ns#type\'>',
             tableLine)

    def parseTableLine(self, isTypeTable, tableLine):

        if isTypeTable:

            tropeNameMatch = re.search('type<\/div><\/td>\s*<td>\s*<a\s+href=\'(.+?)\'>(.+?)<\/a>',
                tableLine, re.MULTILINE)

            if tropeNameMatch:
                self.trope.url = tropeNameMatch.group(1)
                self.trope.name = tropeNameMatch.group(2)
                self.tropeTypeFound = True

            else:
                #@REFACTORING trhow an exception here!
                print '!!!!!!!!!!Exception!!!!!!!!!!'

        elif self.tropeTypeFound:
            tropeCommentMatch = re.search(
                '<div title=\'http:\/\/www\.w3\.org\/2000\/01\/rdf-schema#comment\'>.+?<\/div>\s*<\/td>\s*<td><i>(.+?)</i></td>',
                tableLine, re.MULTILINE)

            if tropeCommentMatch:
                self.trope.comment = tropeCommentMatch.group(1)
                self.tropesList.append(self.trope)
                self.initTempTropeDataStructures()
