# -*- coding: utf-8 -*-
import click
import logging
import requests

@click.command()
def main():
    """ Scrapes Disbiome for the experimental database and extracts the
        specific microbes associated with both Crohn's Disease and Ulcerative Colitis.
    """
    logger = logging.getLogger(__name__)
    logger.info('downloading Disbiome experimental dataset')

    r = requests.get(url='https://disbiome.ugent.be:8080/experiment')

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
