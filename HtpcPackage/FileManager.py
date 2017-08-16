import sys
import os
import datetime
# from os.path import join, getsize
import shutil
import logging


class Filemanager(object):
    """Filemanager Class"""
    # sourcePath = "C:\TestFileshare"
    sourcePath = "/media/daten/downloads/complete"
    extension = ".mkv"

    def main(self):
        print("Trying to move Files in Path \"" + self.sourcePath + "\" with extension \"" + self.extension + "\"")
        try:
            # print(sys.argv)
            (scriptname, directory, orgnzbname, jobname, reportnumber, category, group, postprocstatus, url) = sys.argv
            print(scriptname, directory, orgnzbname, jobname, reportnumber, category, group, postprocstatus, url)
            destinationPath = self._evaluateDestinationPath(category)

        except:
            print("No commandline parameters found")
            # raise(Exception("asujifkh"))

        #    sys.exit(1)
        # continue script
        counter = 0
        for root, dirs, files in os.walk(self.sourcePath):
            for file in files:
                if file.endswith(self.extension):
                    print(os.path.join(root, file))
                    # self._copyFile(file, destinationPath)
                    counter += 1
        print(str(counter) + " files have been moved")
        # Success code
        # sys.exit(0)
        return

    def _evaluateDestinationPath(self, category):
        """Gets the Destination path depending on the type of the movie and the actual year of the download"""
        if category == "movie":
            # catPath = "filme\\" + datetime.datetime.now().year.__str__()
            catPath = "filme/" + datetime.datetime.now().year.__str__()
        # if category == "tv":
        #     raise Exception("Category not Supported")
        else:
            raise Exception("Category not Supported")
        # evalPath = "C:\\TestFileshare\\Destination\\" + catPath + "\\"
        evalPath = "/media/daten/tv/" + catPath
        print("Destination-Path: \"" + evalPath + "\"")
        return evalPath
        pass

    def _copyFile(self, file, destinationPath):
        """Copy Files from source to destination"""
        shutil.copy(file, destinationPath)

        pass


if __name__ == '__main__':
    Filemanager().main()


    # print(root, "consumes", end = "")
    # print(sum([os.path.getsize(os.path.join(root, name)) for name in
    # files]), end="")
    # print("bytes in", len(files), "non-directory files")
    # if 'CVS' in dirs:
    #    dirs.remove('CVS') # don't visit CVS directories
