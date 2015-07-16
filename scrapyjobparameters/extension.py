import logging, os

logger = logging.getLogger(__name__)

class JobParametersExtension(object):

    @classmethod
    def from_crawler(cls, crawler):
        # instantiate the extension object
        ext = cls()

        sp = crawler.spider
        sp.job_id = os.environ.get('SCRAPY_JOB')
        sp.project_id = os.environ.get('SCRAPY_PROJECT_ID')

        # return the extension object
        return ext