import logging, os
from scrapy import signals
logger = logging.getLogger(__name__)

class JobParametersExtension(object):

    @classmethod
    def from_crawler(cls, crawler):
        # instantiate the extension object
        ext = cls()

        #connect the extension object to signals
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)

        # return the extension object
        return ext

    def spider_opened(self, spider):
        logger.info('TEST')
        spider.job_id = os.environ.get('SCRAPY_JOB')
        spider.project_id = os.environ.get('SCRAPY_PROJECT_ID')
