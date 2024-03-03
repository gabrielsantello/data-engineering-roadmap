from loguru import logger
from functools import wraps

logger.remove()

logger.add(
                "my_log_file.log",
                format="{time} {level} {message} {file}",
                level="INFO"
            )

logger.add(
                "my_critical_log_file.log",
                format="{time} {level} {message} {file}",
                level="INFO"
            )

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Calling function '{func.__name__}' with args {args} and kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Function '{func.__name__}' returned {result}")
            return result
        except Exception as e:
            logger.exception(f"Exception caught in '{func.__name__}': {e}")
            raise  # Re-raise the exception to not alter the behavior of the decorated function
    return wrapper