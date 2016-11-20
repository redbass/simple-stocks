import logging
from pkg_resources import resource_filename


ROOT_PATH = resource_filename(__name__, '')
logging.basicConfig(level=logging.INFO)
