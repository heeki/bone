import logging
from datetime import datetime


class Global:
    def __init__(self):
        pass

    @staticmethod
    def get_logger(name, file_local):
        log = logging.getLogger(name)
        log_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s '%(message)s'")

        handler_console = logging.StreamHandler()
        handler_console.setFormatter(log_formatter)
        handler_file = logging.FileHandler(file_local)
        handler_file.setFormatter(log_formatter)

        # if len(log.handlers) == 0:
        #     log.addHandler(handler_console)
        #     log.addHandler(handler_file)

        log.setLevel(logging.INFO)
        return log

    @staticmethod
    def gen_timestamp():
        """ Generate a timestamp

        :return: timestamp string
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

