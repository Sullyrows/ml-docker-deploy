import logging 

logger = logging.getLogger("flask")
logger.setLevel(logging.DEBUG)

# set formatter for just time 
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    datefmt='%H:%M:%S'
)
# create console handler and set formatter
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)