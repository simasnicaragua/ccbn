# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Departamento'
        db.create_table('lugar_departamento', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True, db_index=True)),
            ('extension', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('lugar', ['Departamento'])

        # Adding model 'Municipio'
        db.create_table('lugar_municipio', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Departamento'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True, db_index=True)),
            ('extension', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('latitud', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('longitud', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
        ))
        db.send_create_signal('lugar', ['Municipio'])

        # Adding model 'Ciudad'
        db.create_table('lugar_ciudad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Municipio'])),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('lugar', ['Ciudad'])

        # Adding model 'Barrio'
        db.create_table('lugar_barrio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Ciudad'])),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('lugar', ['Barrio'])


    def backwards(self, orm):
        
        # Deleting model 'Departamento'
        db.delete_table('lugar_departamento')

        # Deleting model 'Municipio'
        db.delete_table('lugar_municipio')

        # Deleting model 'Ciudad'
        db.delete_table('lugar_ciudad')

        # Deleting model 'Barrio'
        db.delete_table('lugar_barrio')


    models = {
        'lugar.barrio': {
            'Meta': {'object_name': 'Barrio'},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Ciudad']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        'lugar.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['lugar']
