import yaml
import logging
import logging.config


def main():

    with open('logging.conf.yaml','r') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
        logging.config.dictConfig(config)
        logger = logging.getLogger('simpleExample')

        logger.debug("TESTING")

if __name__ == '__main__':
    main()

