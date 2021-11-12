import unittest
import assignment_seven


class MyTestCase(unittest.TestCase):

    def test_encode_two(self):
        self.assertEqual("rmflcfp", assignment_seven.encode_decode(True, "Pycharm", "code"))
        self.assertEqual("wcescjdpek", assignment_seven.encode_decode(True, "hello world", "python"))
        self.assertEqual("hzbjquhuwgvzkjzggxaguhwgtm", assignment_seven.encode_decode(True, "this is a generic long sentence", "ostrich"))

    def test_decode_two(self):
        self.assertEqual("airplane", assignment_seven.encode_decode(False, "bwrimonx", "boat"))
        self.assertEqual("unitseven", assignment_seven.encode_decode(False, "ufabyrhia", "assignment"))
        self.assertEqual("unittestsareimportantwaystomakesurethatyourfunctionactsasexpected", assignment_seven.encode_decode(False, "xrkkrtlwwcicxfsstkycmzeajrdfdogjsgxwlckwdnujweaibrrctrhtvizgcrmhh", "decrypt"))




if __name__ == '__main__':
    unittest.main()
