import inspect

import softest
import logging


class Utils(softest.TestCase):

    def Assert(self, actual, expected):
        self.soft_assert(self.assertEqual, actual, expected)

    def custom_loggers(self, logLevel=logging.DEBUG):
        # set a class/method from where the logger is called
        logger_name = inspect.stack()[1][3]
        # create a logger
        logger = logging.getLogger(logger_name)
        # set a log level
        logger.setLevel(logLevel)
        # add a handler
        ch = logging.StreamHandler()
        fh = logging.FileHandler(filename='..//loggers//log.log')
        # set a formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
        # add formatter to the handler
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        # add handler to the logger
        logger.addHandler(ch)
        logger.addHandler(fh)
        return logger
