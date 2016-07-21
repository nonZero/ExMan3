from django.test import TestCase


class SimpleViewsTestCase(TestCase):
    def test_stars(self):
        url = "/stars/5/"
        r = self.client.get(url)
        # self.assertEquals(r.status_code, 200)
        # self.assertEquals(r.content.decode(), 'KUKU! *****')
        self.assertContains(r, 'KUKU! *****')
