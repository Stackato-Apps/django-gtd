# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Project'
        db.create_table('gtd_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('deadline', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('gtd', ['Project'])

        # Adding model 'Context'
        db.create_table('gtd_context', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('gtd', ['Context'])

        # Adding model 'Thing'
        db.create_table('gtd_thing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtd.Project'], null=True, blank=True)),
            ('context', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtd.Context'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('archived', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('progress', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('schedule', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('gtd', ['Thing'])

        # Adding model 'Reminder'
        db.create_table('gtd_reminder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('thing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtd.Thing'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('unit', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('method', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('gtd', ['Reminder'])


    def backwards(self, orm):
        
        # Deleting model 'Project'
        db.delete_table('gtd_project')

        # Deleting model 'Context'
        db.delete_table('gtd_context')

        # Deleting model 'Thing'
        db.delete_table('gtd_thing')

        # Deleting model 'Reminder'
        db.delete_table('gtd_reminder')


    models = {
        'gtd.context': {
            'Meta': {'object_name': 'Context'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '90'})
        },
        'gtd.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '90'})
        },
        'gtd.reminder': {
            'Meta': {'object_name': 'Reminder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'thing': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtd.Thing']"}),
            'unit': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        },
        'gtd.thing': {
            'Meta': {'object_name': 'Thing'},
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtd.Context']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'progress': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtd.Project']", 'null': 'True', 'blank': 'True'}),
            'schedule': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['gtd']
