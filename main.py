import threading
from queue import Queue
from spider import Spider
from domain import *
from crawler import *
"""

"""

#no constants in python, hence all are CAPS to indicate constant in python
PROJECT_NAME = 'youtube'
HOMEPAGE = 'https://www.youtube.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
