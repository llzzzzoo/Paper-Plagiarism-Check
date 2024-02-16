import unittest
from main import EmptyException
from main import check_empty
from main import caculate_similarity
from main import participle
from main import read_file
from main import save_file
from main import main


class TestStringMethods(unittest.TestCase):
    def test_checkEmpty(self):
        with self.assertRaises(EmptyException):
            check_empty('')

    def test_calculate_type(self):
        s = caculate_similarity('元氏人', '什么档次')
        self.assertEqual(s, TypeError)

    def test_calculate_output(self):
        s = caculate_similarity([('呵呵', 0.5), ('桀桀', 0.5)], [('在吗', 0.2), ('消愁', 0.8)])
        self.assertEqual(s, 0.48484848484848486)  # Output should be 0.48484848484848486

    def test_calculate_empty(self):
        s = caculate_similarity([], [])
        self.assertEqual(s, EmptyException)

    def test_participle_type(self):
        s = participle(1)
        self.assertEqual(s, TypeError)

    def test_participle_empty(self):
        s = participle('')
        self.assertEqual(s, EmptyException)

    def test_read_fileNotFound(self):
        s = read_file('where are you now')
        self.assertEqual(s, FileNotFoundError)

    def test_read_empty(self):
        s = read_file('test_empty.txt')
        self.assertEqual(s, EmptyException)

    def test_save_type(self):
        s = save_file('output.txt', 'test')
        self.assertEqual(s, TypeError)

    def test_save_value_upperOne(self):
        s = save_file('output.txt', 1.1)
        self.assertEqual(s, ValueError)

    def test_save_value_lowerZero(self):
        s = save_file('output.txt', -0.1)
        self.assertEqual(s, ValueError)

    def test_main_type(self):
        original_text_path = 1
        plagiarized_text_path = 1
        output_text_path = 1
        args = ['main.py', original_text_path, plagiarized_text_path, output_text_path]
        s = main(args)
        self.assertEqual(s, TypeError)

    def test_main_normal(self):
        original_text_path = 'orig.txt'
        plagiarized_text_path = 'orig_0.8_add.txt'
        output_text_path = 'output.txt'
        args = ['main.py', original_text_path, plagiarized_text_path, output_text_path]
        s = main(args)
        self.assertEqual(s, 1)


if __name__ == '__main__':
    unittest.main()
