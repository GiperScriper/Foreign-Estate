# -*- coding: utf-8 -*-
from django.db.models import Q

# Cортировка по площади и цене
def sortBuy(qs, params):
    sort_type = params['sort_type']    
    
    if 'price_sell_u' in sort_type:
        qs = qs.order_by(sort_type)
    elif 'area_object' in sort_type:
        qs = qs.exclude(area_object__isnull=True).order_by(sort_type) 
    return qs
    

def sortRent(qs, params):
    sort_type = params['sort_type']
    
    if 'price_rent_monthly' in sort_type:
        qs = qs.order_by(sort_type)
    elif 'area_object' in sort_type:
        qs = qs.exclude(area_object__isnull=True).order_by(sort_type)    
    return qs


# Фильтруем по полю purpose
def filterByPurpose(qs, params):
    purpose = params['purpose']
    if purpose == 's':
        qs = qs.filter(purpose__in = ['s', 'sr'])
    elif purpose == 'r':
    	qs = qs.filter(purpose__in = ['r', 'sr'])
    return qs


# Фильтруем по полю country
def filterByCountry(qs, params):
	countries = params['countries']
	if countries:
		qs = qs.filter(country__in = countries)
	return qs


# Фильтруем в списке значений (страны)
def filterByFieldWithEnum(qs, params, param_name, field_name):
	filterEnum = params[param_name]
	if filterEnum:
		qs = qs.filter( **{"{0}__in".format(field_name): filterEnum} )
	return qs


# Фильтурем в промежутке значений (площадь, цена и тд.)
def filterByFieldWithRange(qs, params, param_name, field_name):
    filterRange = params[param_name]
    if filterRange:
        qs = qs.filter( **{"{0}__range".format(field_name): (filterRange[0], filterRange[1])} )  
    return qs


# Фильтруем по количеству комнат
def filterByRoomAmount(qs, params, max_value):
    room_amount = params['room_amount']    
    if len(room_amount) == 0:
        return qs

    filterExpr = Q(rooms_living__in = room_amount)
    	
    if max_value in room_amount:			 
       filterExpr = filterExpr | Q(rooms_living__gt = max_value)					

    return qs.filter(filterExpr)


# Фильтруем по особенностям
def filterByFeatures(qs, params): 
    features = params['features']
    if features:
        kwargs = {}
        for param in features:
            kwargs[param] = 1
        qs = qs.filter( **kwargs )
    return qs  