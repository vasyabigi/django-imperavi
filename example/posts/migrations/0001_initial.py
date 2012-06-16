# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table('posts_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('posts', ['Article'])

        # Adding model 'Post'
        db.create_table('posts_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['posts.Article'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('posts', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table('posts_article')

        # Deleting model 'Post'
        db.delete_table('posts_post')


    models = {
        'posts.article': {
            'Meta': {'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'posts.post': {
            'Meta': {'object_name': 'Post'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['posts.Article']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['posts']