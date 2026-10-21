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


    def test_documentation_integrity(self):
        required_docs = [
            self.root / 'AGENTS.md',
            self.root / 'docs' / 'ARCHITECTURE.md',
            self.root / 'docs' / 'AGILE_WORKFLOW.md',
            self.root / 'docs' / 'HOSTING_STRATEGY.md',
            self.root / 'docs' / 'BACKLOG.md',
            self.root / '.github' / 'PULL_REQUEST_TEMPLATE.md',
            self.root / '.github' / 'ISSUE_TEMPLATE' / 'feature_request.md',
            self.root / '.github' / 'ISSUE_TEMPLATE' / 'bug_report.md',
            self.root / '.github' / 'ISSUE_TEMPLATE' / 'task.md',
        ]
        for doc in required_docs:
            self.assertTrue(doc.exists(), f'Missing required documentation file: {doc}')
            self.assertGreater(doc.stat().st_size, 50, f'Documentation file should not be empty: {doc}')


if __name__ == '__main__':
    unittest.main()
