# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RegisterInfo.timestamp'
        db.delete_column(u'app_registerinfo', 'timestamp')

        # Adding field 'RegisterInfo.last_modified'
        db.add_column(u'app_registerinfo', 'last_modified',
                      self.gf('django.db.models.fields.TimeField')(auto_now=True, default=datetime.datetime(2014, 8, 2, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'RegisterInfo.timestamp'
        raise RuntimeError("Cannot reverse this migration. 'RegisterInfo.timestamp' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'RegisterInfo.timestamp'
        db.add_column(u'app_registerinfo', 'timestamp',
                      self.gf('django.db.models.fields.TimeField')(auto_now_add=True, blank=True),
                      keep_default=False)

        # Deleting field 'RegisterInfo.last_modified'
        db.delete_column(u'app_registerinfo', 'last_modified')


    models = {
        u'app.registerinfo': {
            'Meta': {'object_name': 'RegisterInfo'},
            'date': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'graduate': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'jobtime': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'last_modified': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'question1': ('django.db.models.fields.TextField', [], {}),
            'question2': ('django.db.models.fields.TextField', [], {}),
            'question3': ('django.db.models.fields.TextField', [], {}),
            'referrer': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'resume': ('django.db.models.fields.TextField', [], {}),
            'separate': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'workplace': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'app.registration': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Registration', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'response': ('mezzanine.core.fields.RichTextField', [], {})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['app']