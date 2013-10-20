# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'dataminas_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['dataminas.Category'], null=True, blank=True)),
        ))
        db.send_create_signal(u'dataminas', ['Category'])

        # Adding model 'Point'
        db.create_table(u'dataminas_point', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('month', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=32, decimal_places=2)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dataminas.Category'])),
            ('user_score', self.gf('django.db.models.fields.IntegerField')()),
            ('algorithm_score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'dataminas', ['Point'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'dataminas_category')

        # Deleting model 'Point'
        db.delete_table(u'dataminas_point')


    models = {
        u'dataminas.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['dataminas.Category']", 'null': 'True', 'blank': 'True'})
        },
        u'dataminas.point': {
            'Meta': {'object_name': 'Point'},
            'algorithm_score': ('django.db.models.fields.IntegerField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dataminas.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.IntegerField', [], {}),
            'user_score': ('django.db.models.fields.IntegerField', [], {}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '32', 'decimal_places': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['dataminas']