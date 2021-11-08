import unittest
import strings_one


class MyTestCase(unittest.TestCase):

    def test_half_slice_even(self):
        self.assertEqual("utercomp", strings_one.half_slice("computer"))
        self.assertEqual("ih", strings_one.half_slice("hi"))
        self.assertEqual("erflybutt", strings_one.half_slice("butterfly"))
        self.assertEqual("anc", strings_one.half_slice("can"))


    def test_no_first_last(self):
        self.assertEqual("ompute", strings_one.no_first_last("computer"))
        self.assertEqual("", strings_one.no_first_last("hi"))
        self.assertEqual("utterfl", strings_one.no_first_last("butterfly"))
        self.assertEqual("a", strings_one.no_first_last("can"))

    def test_longest_word(self):
        phrase1 = "Whether you think you can or you think you can't, you're right"
        phrase2 = "I have learned over the years that when one's mind is made up, this diminishes fear"
        phrase3 = "You may be disappointed if you fail, but you are doomed if you don't try"
        self.assertEqual(7, strings_one.longest(phrase1))
        self.assertEqual(10, strings_one.longest(phrase2))
        self.assertEqual(12, strings_one.longest(phrase3))

    def test_title_case(self):
        phrase1 = "Whether you think you can or you think you can't, you're right"
        phrase1_cap = "Whether You Think You Can Or You Think You Can't, You're Right"
        phrase2_cap = "I Have Learned Over The Years That When One's Mind Is Made Up, This Diminishes Fear"
        phrase2 = "I have learned over the years that when one's mind is made up, this diminishes fear"
        phrase3 = "You may be disappointed if you fail, but you are doomed if you don't try"
        phrase3_cap = "You May Be Disappointed If You Fail, But You Are Doomed If You Don't Try"
        self.assertEqual(phrase1_cap, strings_one.title_case(phrase1))
        self.assertEqual(phrase2_cap, strings_one.title_case(phrase2))
        self.assertEqual(phrase3_cap, strings_one.title_case(phrase3))


if __name__ == '__main__':
    unittest.main()
