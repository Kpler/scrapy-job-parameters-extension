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
        job_name = os.environ.get('SCRAPY_JOB')

        #for ScrapingHub, job id is 'PROJECT_ID/SPIDER_ID/JOB_ID'
        try:
            (project_id, spider_id, job_id) = job_name.split('/')
        except ValueError:
            # if not enpught value to unpack this is not a SH id, so keep the all string
            job_id = job_name
            spider_id = None
            project_id = os.environ.get('SCRAPY_PROJECT_ID')

        spider.project_id = project_id
        spider.spider_id = spider_id
        spider.job_id = job_id

        logger.info('Project id : {}'.format(spider.project_id))
        logger.info('Spider id : {}'.format(spider.spider_id))
        logger.info('Job id : {}'.format(spider.job_id))
