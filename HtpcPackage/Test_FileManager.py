import unittest
import sys
from HtpcPackage import FileManager as filemanager


class TestFileManager(unittest.TestCase):
    """Testsclass for FileManager Unittests"""
    fm = filemanager.Filemanager()

    def setUp(self):
        pass

    def test_FileManager_evaluateDestination_Movie(self):
        evalPath = self.fm._evaluateDestinationPath("movie")
        self.assertTrue(evalPath.__contains__("\\filme\\2017\\"))
        return

    def test_copyFiles(self):
        self.fm._copyFile("s","")

    def test_FileManager_main(self):
        # FileManager.main(scriptname = "scriptname" ,directory =
        # "dir",orgnzbname="orgnzbname",jobname="jobname",reportnumber="reportnumber",category="category",
        #                   group="group",postprocstatus="postprocstatus",url="url")
        # sys.argv = ["scriptname", "dir"]
        self.fm.main()
        # self.assertEqual(s, "hallobla")
        return

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
