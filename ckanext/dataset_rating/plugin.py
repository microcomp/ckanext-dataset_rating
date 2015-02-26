import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic as logic

import ckan.logic
import ckan.model as model
from ckan.common import _, c
import logging
import rating



class DatasetRatingPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
    def before_map(self, map):
        map.connect('rate_dataset', '/dataset/rate/', action='RateDataset', controller="ckanext.dataset_rating.rating:RatingController")
        
        return map
    def get_helpers(self):
    	return {'avg': rating.avg,
    			'can_rate': rating.can_rate}
