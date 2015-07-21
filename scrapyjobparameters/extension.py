import logging, os
from scrapy import signals
logger = logging.getLogger(__name__)

class JobParametersExtension(object):

    def __init__(self):
        (project_id, spider_id, job_id) = self.retrieve_info()
        self.project_id = project_id
        self.spider_id = spider_id
        self.job_id = job_id
        logger.info('Project id : {}'.format(self.project_id))
        logger.info('Spider id : {}'.format(self.spider_id))
        logger.info('Job id : {}'.format(self.job_id))

    @classmethod
    def from_crawler(cls, crawler):
        # instantiate the extension object
        ext = cls()

        #connect the extension object to signals
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)

        # return the extension object
        return ext

    def spider_opened(self, spider):
        spider.project_id = self.project_id
        spider.spider_id = self.spider_id
        spider.job_id = self.job_id

    @classmethod
    def retrieve_info(cls):
        job_name = os.environ.get('SCRAPY_JOB')

        #for ScrapingHub, job id is 'PROJECT_ID/SPIDER_ID/JOB_ID'
        try:
            (project_id, spider_id, job_id) = job_name.split('/')
        except (ValueError, AttributeError):
            # if not enough value to unpack this is not a SH id, so keep the all string
            job_id = job_name
            spider_id = None
            project_id = os.environ.get('SCRAPY_PROJECT_ID')

        os.environ['SCRAPY_PROJECT_ID'] = project_id
        os.environ['SCRAPY_JOB_ID'] = job_id
        os.environ['SCRAPY_SPIDER_ID'] = spider_id

        return project_id, spider_id, job_id