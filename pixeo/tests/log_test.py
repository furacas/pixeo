import multiprocessing
import unittest

import pixeo.log as log


def worker_task(queue):
    log.setup_logger(queue)

    logger = log.get_logger(__name__)  # get a logger

    # log some messages
    logger.debug('This is a debug message.')
    logger.info('This is an info message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
    logger.critical('This is a critical message.')


class TestGPS(unittest.TestCase):

    def test_log(self):
        queue = multiprocessing.Queue(-1)
        listener = log.setup_listener(queue)

        worker = multiprocessing.Process(target=worker_task, args=(queue,))
        worker.start()
        worker.join()

        queue.put_nowait(None)
        listener.join()
