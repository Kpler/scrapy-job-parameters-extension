import unittest, os

from scrapy.conf import settings
from scrapy.spiders import Spider
from scrapy.crawler import Crawler
from scrapy.exceptions import NotConfigured

from scrapyjobparameters.extension import JobParametersExtension


class SimpleSpiderTest(Spider):
    name = 'test'

class TestLogentriesExtension(unittest.TestCase):

    def setUp(self):
        os.environ['SCRAPY_JOB'] = 'id1'
        os.environ['SCRAPY_PROJECT_ID'] = 'id2'

    def test_parameters(self):
        crawler = Crawler(SimpleSpiderTest, settings)
        extension = JobParametersExtension.from_crawler(crawler)
        crawler.crawl()
        self.assertEqual(crawler.spider.job_id, 'id1')
        self.assertEqual(crawler.spider.project_id, 'id2')
