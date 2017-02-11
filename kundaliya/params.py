import logging
import yaml
import os

logger = logging.getLogger(__name__)


class Params:
    """ Object containing build parameters to be used in the build process.
     Parameters are captured from setting.yaml file.
    """

    def __init__(self, path=None):
        logging.basicConfig(level=logging.WARNING)
        logger.info("Acquiring settings")
        settings = None
        if path == None:
            path = "settings.yaml"
            self.cwd=os.getcwd()
        else:
            self.cwd=os.path.dirname(path)

        try:
            with open(path, 'r') as f:
                doc = yaml.load(f)
                self.__dict__.update(doc)
        except IOError:
            logger.error("No settings.yaml found")
        except yaml.YAMLError:
            logger.error("YAML error")
        except RuntimeError as e:
            logger.error("Unknown Error", e)
