# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import ckan.model as model
import ckan.logic as logic
import ckan.lib.base as base
import ckan.lib.helpers as h
import ckan.lib.navl.dictization_functions as df
import ckan.plugins as p
from ckan.common import _, c, g
import ckan.plugins.toolkit as toolkit


import uuid
import logging
import ckan.logic
'''
TODO:
-db table
-check acces (helper)
-if RateDataset
-mod/new rating
-current rating (helper)

'''
class RatingController(base.BaseController):
    def RateDataset(self):
        rating = logic.clean_dict(df.unflatten(logic.tuplize_dict(logic.parse_params(base.request.params))))
        logging.warning('MAJOM')
        logging.warning(rating)
        related_id = rating['dataset_id']
        return h.redirect_to(controller='package', action='read', id=related_id)