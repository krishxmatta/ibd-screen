# -*- coding: utf-8 -*-
import click
import logging
import pandas as pd
import requests

@click.command()
@click.argument('output_directory', type=click.Path())
def main(output_directory):
    """ Scrapes Disbiome for the experimental database and extracts the
        specific microbes associated with both Crohn's Disease and Ulcerative Colitis.
    """
    logger = logging.getLogger(__name__)
    logger.info('downloading Disbiome experimental dataset')

    r = requests.get(url='https://disbiome.ugent.be:8080/experiment')

    logger.info('scraping the Disbiome experimental dataset')

    df = pd.json_normalize(r.json())

    ibd_microbes = df[(df['disease_id'] == 3) | (df['disease_id'] == 4)]['organism_name'].copy()
    ibd_microbes.drop_duplicates(inplace=True)
    ibd_microbes.to_csv(f'{output_directory}/ibd_microbes.csv')

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
