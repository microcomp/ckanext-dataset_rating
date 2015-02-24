import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic as logic

import ckan.logic
import ckan.model as model
from ckan.common import _, c
import logging


class DatasetRatingPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
    def before_map(self, map):
        map.connect('rate_dataset', '/dataset/rate/', action='RateDataset', controller="ckanext.dataset_rating.rating:RatingController")
        
        return map
