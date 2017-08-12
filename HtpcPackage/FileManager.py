import sys
import os
# from os.path import join, getsize
import shutil
import logging


class FileManager:
    """Filemanager Class"""
    sourcePath = "C:\TestFileshare"
    # sourcePath = "/media/daten/downloads/complete"
    # destinationPath
    extension = ".mkv"

    def main(self):
        try:
            # print(sys.argv)
            (scriptname, directory, orgnzbname, jobname, reportnumber
             , category, group, postprocstatus, url) = sys.argv
            print(scriptname, directory, orgnzbname, jobname, reportnumber
                  , category, group, postprocstatus, url)

        except:
            print("No commandline parameters found")
            # raise(Exception("asujifkh"))

        #    sys.exit(1)
        # continue script

        destinationPath = self.__evaluateDestinationPath()

        # Iterate through all files in all subfolders of root incl. root
        for root, dirs, files in os.walk(self.sourcePath):
            for file in files:
                if (file.endswith(self.extension)):
                    print(os.path.join(root, file))
                    self.__copyFile(file, destinationPath)

                    # print(root, "consumes", end = "")
                    # print(sum([os.path.getsize(os.path.join(root, name)) for name in
                    # files]), end="")
                    # print("bytes in", len(files), "non-directory files")
                    # if 'CVS' in dirs:
                    #    dirs.remove('CVS') # don't visit CVS directories
                    # Your code goes here

        # Success code
        # sys.exit(0)
        return

    def __copyFile(self, filePath, destinationPath):
        """Copy Files from source to destination"""
        pass

    def __evaluateDestinationPath(self):
        """Gets the Destination path depending on the type of the movie
            and the actual year of the download"""
        pass

    if __name__ == '__main__':
        main()
