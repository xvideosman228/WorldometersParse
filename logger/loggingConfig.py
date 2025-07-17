import logging.config
import json
from functools import wraps

with open('logger/loggerConfig.json') as conf:
    logConfig = json.load(conf)


logging.config.dictConfig(logConfig)
logger = logging.getLogger('logger')


def exception(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            await func(*args, **kwargs)
        except Exception:
            err = f"Исключение появилось: {func.__name__}"
            logger.exception(err)
    return wrapper