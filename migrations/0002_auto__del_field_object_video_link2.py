# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Object.video_link2'
        db.delete_column(u'foreign_estate_object', 'video_link2')


    def backwards(self, orm):
        # Adding field 'Object.video_link2'
        db.add_column(u'foreign_estate_object', 'video_link2',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    models = {
        u'foreign_estate.object': {
            'Meta': {'object_name': 'Object'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'area_land': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'area_living': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'area_object': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'balcony': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bathrooms': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'construction_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description_full': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_short': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'distance_mountains': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'distance_parking': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'distance_sea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'distance_supermarket': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_line': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fitness': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'floor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'floors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'furnished': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'garage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'garage_cars': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'garden': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'golf': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'golf_field': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'object_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'parking': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'personal_beach': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'photos': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pool': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'price_rent_monthly': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price_rent_weekly': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price_sell': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price_sell_e': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price_sell_r': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price_sell_u': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'private_beach': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'private_gym': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'private_pier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'private_tennis_court': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'private_territory': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'rooms_balcony': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rooms_combined': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rooms_living': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rooms_sauna': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rooms_terrace': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'supermarket': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'terrace': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tv': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'video_link': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'window_view': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['foreign_estate']