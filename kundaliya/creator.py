import logging

logger=logging.getLogger(__name__)

class Params:
    def __init__(self, path=None):
        logging.basicConfig(level=logging.WARNING)
        logger.info("Acquiring settings")
        settings=None
        if path==None:
            path="settings.yaml"
        try:
            settings=open(path)
        except IOError:
            logger.error("No settings.yaml found")
