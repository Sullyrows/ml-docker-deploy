import logging 

logger = logging.getLogger("model")
logger.setLevel(logging.DEBUG)

# set formatter for just time 
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    datefmt='%H:%M:%S'
)
logger.setFormatter(formatter)
