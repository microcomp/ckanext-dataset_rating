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

import db

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
def create_dataset_rating_table(context):
    if db.dataset_rating_table is None:
        db.init_db(context['model'])

@ckan.logic.side_effect_free
def in_rating_db(context, data_dict):
    create_dataset_rating_table(context)
    if data_dict['user_id'] == None or data_dict['user_id'] == '':
        return False
    res = db.DatasetRating.get(**data_dict)
    if res:
        for i in res:
            if i.user_id == data_dict['user_id']:
                return True

    return False

def can_rate(user_id):
    context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author, 'auth_user_obj': c.userobj,
                   'for_view': True}
    try:
        logic.check_access('tags_admin', context)
        return True
    except logic.NotAuthorized:
        return False
    return False
def avg(dataset_id):
    context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author, 'auth_user_obj': c.userobj,
                   'for_view': True}
    data_dict = {'dataset_id': dataset_id}
    create_dataset_rating_table(context)

    result = db.DatasetRating.get(**data_dict)
    
    if len(result) != 0:
        sum=0.0
        for i in result:
            sum+=float(i.rating)

        return sum/len(result)
    else:
        return 0;

@ckan.logic.side_effect_free
def new_rating(context, data_dict):
    create_dataset_rating_table(context)
    data_dict2 = {'dataset_id':data_dict['dataset_id'], 'user_id':data_dict['user_id']}
    if in_rating_db(context, data_dict2):
        res = db.DatasetRating.get(**data_dict2)[0]
        res.rating = data_dict['rating']
        res.save()
        session = context['session']
        session.commit()
    else:
        info = db.DatasetRating()
        info.id = unicode(uuid.uuid4()) 
        info.user_id = data_dict['user_id']
        info.dataset_id = data_dict['dataset_id']
        info.rating = data_dict['rating']
        info.save()
        session = context['session']
        session.add(info)
        session.commit()
    return {"status":"success"}


class RatingController(base.BaseController):
    def RateDataset(self):
    	context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author, 'auth_user_obj': c.userobj,
                   'for_view': True}
        rating = logic.clean_dict(df.unflatten(logic.tuplize_dict(logic.parse_params(base.request.params))))
        logging.warning(rating)
        dataset_id = rating['dataset_id']
        rating = rating['value']
        data_dict = {'rating': rating, 'dataset_id':dataset_id, 'user_id':c.userobj.id}
        new_rating(context, data_dict)

        return h.redirect_to(controller='package', action='read', id=dataset_id)