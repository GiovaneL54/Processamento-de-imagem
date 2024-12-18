import unittest
from  image_processing.processing import load_image

class TestProcessing(unittest.TestCase):
    def test_load_image(self):
        img = load_image('path/to/image.jpg')
        self.assertIsNotNone(img)


        if __name__ == '__main__':
            unittest()
