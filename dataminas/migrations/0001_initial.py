# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Point'
        db.create_table(u'dataminas_point', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('x', self.gf('django.db.models.fields.DateField')()),
            ('y', self.gf('django.db.models.fields.DecimalField')(max_digits=32, decimal_places=2)),
        ))
        db.send_create_signal(u'dataminas', ['Point'])


    def backwards(self, orm):
        # Deleting model 'Point'
        db.delete_table(u'dataminas_point')


    models = {
        u'dataminas.point': {
            'Meta': {'object_name': 'Point'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'x': ('django.db.models.fields.DateField', [], {}),
            'y': ('django.db.models.fields.DecimalField', [], {'max_digits': '32', 'decimal_places': '2'})
        }
    }

    complete_apps = ['dataminas']