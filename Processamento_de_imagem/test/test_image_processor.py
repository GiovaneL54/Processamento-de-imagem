import unittest
from image_processor.filters import apply_filter
from image_processor.transformations import resize_image

class TestImageProcessor(unittest.TestCase):
    def test_apply_filter(self):
        result = apply_filter('test_image.jpg', 'BLUR')
        self.assertInstance(result, Image.Image)

    def test_resize_image(self):
        result = resize_image('test_image.jpg', 100,100)
        self.assertEqual(result.size, (100,100))
if __name__ == '__main__':
    unittest.main()