import unittest
from pathlib import Path


class WebsiteValidationTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).parents[1]
        self.html_file = self.root / 'src' / 'index.html'

    def test_html_file_exists_and_is_not_empty(self):
        self.assertTrue(self.html_file.exists(), 'src/index.html must exist')
        self.assertGreater(self.html_file.stat().st_size, 500, 'src/index.html should not be empty')

    def test_html_structure(self):
        content = self.html_file.read_text(encoding='utf-8')
        self.assertIn('<!doctype html>', content.lower(), 'Missing doctype declaration')
        self.assertIn('<html', content.lower(), 'Missing html tag')
        self.assertIn('<head>', content.lower(), 'Missing head tag')
        self.assertIn('<body>', content.lower(), 'Missing body tag')

    def test_site_identity_and_components(self):
        content = self.html_file.read_text(encoding='utf-8')
        self.assertIn('myty.world', content, 'Missing reference to myty.world')
        self.assertIn('calculator', content.lower(), 'Missing calculator section')
        self.assertIn('id="calcResult"', content, 'Missing calculator display element')

    def test_dockerfile_exists(self):
        dockerfile = self.root / 'Dockerfile'
        self.assertTrue(dockerfile.exists(), 'Dockerfile must exist in root')
        content = dockerfile.read_text(encoding='utf-8')
        self.assertIn('FROM', content, 'Dockerfile must contain FROM instruction')
        self.assertIn('COPY', content, 'Dockerfile must contain COPY instruction')


if __name__ == '__main__':
    unittest.main()
