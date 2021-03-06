# -*- coding: utf-8 -*-

from checker.backends import BaseBackend
from checker import logger

log = logger.getLogger(__name__)


class Gentoo_cgitBackend(BaseBackend):
    """for projects hosted on gentoo.org"""

    name = 'Gentoo CGit'
    domain = 'gitweb.gentoo.org'
    example = 'https://gitweb.gentoo.org/proj/sandbox.git'

    def __init__(self, url):
        super(Gentoo_cgitBackend, self).__init__()
        self._url = url
        self._rule_type = "xpath"

    def get_urls(self, branch=None):
        return [self._url, self._url + '/log/']

    def get_rules(self):
        log.debug('use %s backend rule for %s package.' %
                  (self.name, self._url.split('/')[-1]))
        return [("substring(//div[@class='content']//tr[@class='nohover'][3]/following::*/td[4]/span/@title, 1, 19)",
                 ""),
                ("substring(//tr[2]/td[4]/span/@title, 1, 19)",
                 "//tr[2]/td[2]/a/@href")]

    @classmethod
    def isrelease(cls, url):
        if cls.domain in url and 'log' in url:
            return False
        else:
            return True
