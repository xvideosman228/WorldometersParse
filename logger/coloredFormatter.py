import logging

class ColoredFormatter(logging.Formatter):
    COLORS = {'DEBUG': '\033[97m', 'INFO': '\033[92m', 'WARNING': '\033[93m',
              'ERROR': '\033[31m', 'CRITICAL': '\033[91;4m'}

    def format(self, record):
        log_fmt = f"{self.COLORS.get(record.levelname, '')}[%(asctime)s][%(levelname).4s] - %(message)s\033[0m"
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

