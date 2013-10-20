# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Point'
        db.delete_table(u'dataminas_point')

        # Adding model 'Anomaly'
        db.create_table(u'dataminas_anomaly', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('data_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user_score', self.gf('django.db.models.fields.IntegerField')()),
            ('algorithm_score', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'dataminas', ['Anomaly'])


    def backwards(self, orm):
        # Adding model 'Point'
        db.create_table(u'dataminas_point', (
            ('y', self.gf('django.db.models.fields.DecimalField')(max_digits=32, decimal_places=2)),
            ('x', self.gf('django.db.models.fields.DateField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'dataminas', ['Point'])

        # Deleting model 'Anomaly'
        db.delete_table(u'dataminas_anomaly')


    models = {
        u'dataminas.anomaly': {
            'Meta': {'object_name': 'Anomaly'},
            'algorithm_score': ('django.db.models.fields.FloatField', [], {}),
            'data_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_score': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['dataminas']