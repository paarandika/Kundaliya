import logging
import yaml

logger=logging.getLogger(__name__)

class Params:
    def __init__(self, path=None):
        logging.basicConfig(level=logging.WARNING)
        logger.info("Acquiring settings")
        settings=None
        if path==None:
            path="settings.yaml"

        try:
            with open(path, 'r') as f:
                doc = yaml.load(f)
                # print doc
        except IOError:
            logger.error("No settings.yaml found")
        except yaml.YAMLError:
            logger.error("YAML error")
        except:
            logger.error("Unknown Error")

