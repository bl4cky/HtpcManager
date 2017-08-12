import unittest
from HtpcPackage import FileManager as filemanager


class TestFileManager(unittest.TestCase):
    """Testsclass for FileManager Unittests"""

    def test_FileManager_evaluateDestination(self):
        pass
        return

    def test_FileManager_main(self):
        # FileManager.main(scriptname = "scriptname" ,directory =
        # "dir",orgnzbname="orgnzbname",jobname="jobname",reportnumber="reportnumber",category="category",
        #                   group="group",postprocstatus="postprocstatus",url="url")
        # sys.argv = ["scriptname", "dir"]
        fm = filemanager.FileManager()
        fm.main();
        # self.assertEqual(s, "hallobla")
        return


if __name__ == '__main__':
    unittest.main()
