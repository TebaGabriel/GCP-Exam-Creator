import logging
import time

def log (func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger('log_decorator')
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt= '%Y-%m-%d %H:%M:%S %z'
        )

        handler = logging.StreamHandler()
        handler.setFormatter(formatter)


        logger.addHandler(handler)
        logger.info(f"{func.__name__} has started!")
        start = time.perf_counter()

        response = func(*args, **kwargs)
        
        end = time.perf_counter()
        logger.info(f"{func.__name__} has finished! The elapsed time was {end - start} seconds.")
        
        return response
    
    return wrapper