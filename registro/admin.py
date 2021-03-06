# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.forms import CheckboxSelectMultiple
from models import *

class RelacionInline(admin.TabularInline):
    model = Relacion
    fk_name = 'owner'
    extra = 1
    verbose_name_plural = u'Personas de su hogar que esten en CCBN'

class ModuloPersonaInline(admin.StackedInline):
    meh = 'redirect_indicator'
    model = ModuloPersona
    verbose_name_plural = u'Programas a los que pertenece'
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

# Inline para registro en Biblioteca
class RegistroBibliotecaInline(admin.StackedInline):
    model = RegistroBiblioteca
    extra = 1
    max_num = 1
    verbose_name_plural = u'Registro en Biblioteca'

# Formacion Basica Inline
class FormacionBasicaInline(admin.TabularInline):
    model = InscripcionCurso
    fields = (('curso', 'becado', 'fecha'),)
    extra = 1
    verbose_name_plural = u'Educación Básica'

    def queryset(self, request):
        # override para mostrar solos los modulos adecuados
        queryset = super(FormacionBasicaInline, self).queryset(request)\
                    .filter(curso__submodulo__code='educacionbasica')

        if not self.has_change_permission(request):
            queryset = queryset.none()
        return queryset 

    def formfield_for_dbfield(self, db_field, **kwargs):
        # override para sobreescribir el form field y agregar la clase CSS chozen
        # para agregar el filtro en los combos
        if db_field.name == 'curso':
            return forms.ModelChoiceField(label='Seleccionar Curso', queryset=Curso.objects.filter(submodulo__code='educacionbasica'), 
                                          widget=forms.Select(attrs={'class': 'chozen'}))
        return super(FormacionBasicaInline, self).formfield_for_dbfield(db_field, **kwargs)

# Formacion Tecnica Vocacional
class FormacionVocacionalInline(admin.TabularInline):
    model = InscripcionCurso
    verbose_name_plural = u'Formación Técnica Vocacional'
    extra = 1    
    fields = (('curso', 'becado', 'fecha'), )

    def queryset(self, request):
        # override para solo mostrar los registros de este Inline Formacion Tecnica Vocacional
        queryset = super(FormacionVocacionalInline, self).queryset(request)\
                    .filter(curso__submodulo__code='formacionvocacional')

        if not self.has_change_permission(request):
            queryset = queryset.none()
        return queryset 

    def formfield_for_dbfield(self, db_field, **kwargs):
        # override para sobreescribir el form field y agregar la clase CSS chozen
        # para agregar el filtro en los combos
        if db_field.name == 'curso':
            return forms.ModelChoiceField(label=u'Seleccionar Curso', queryset=Curso.objects.filter(submodulo__code='formacionvocacional'), 
                                          widget=forms.Select(attrs={'class': 'chozen'}))
        return super(FormacionVocacionalInline, self).formfield_for_dbfield(db_field, **kwargs)

# Formacion Artistica
class FormacionArtisticaInline(admin.TabularInline):
    model = InscripcionCurso
    verbose_name_plural = u'Formación Artística'
    extra = 1    
    fields = (('curso', 'becado', 'fecha'), )

    def queryset(self, request):
        # override para solo mostrar los registros de este Inline Formacion Tecnica Vocacional
        queryset = super(FormacionArtisticaInline, self).queryset(request)\
                    .filter(curso__submodulo__code='formacionartistica')

        if not self.has_change_permission(request):
            queryset = queryset.none()
        return queryset 

    def formfield_for_dbfield(self, db_field, **kwargs):
        # override para sobreescribir el form field y agregar la clase CSS chozen
        # para agregar el filtro en los combos
        if db_field.name == 'curso':
            return forms.ModelChoiceField(label=u'Seleccionar Curso', queryset=Curso.objects.filter(submodulo__code='formacionartistica'), 
                                          widget=forms.Select(attrs={'class': 'chozen'}))
        return super(FormacionArtisticaInline, self).formfield_for_dbfield(db_field, **kwargs)

# Inlines de Registro de Becas
class RegistroBecaPrimariaInline(admin.TabularInline):
    model = RegistroBecaPrimaria
    extra = 1
    exclude = ('tutoria', 'rendimiento_academico', 'recibio_suplemento', 
               'recibio_atencion_psicologica', 'mejoro_habilidades', 'reconoce_capacidad', 'perc_derecho')
    verbose_name_plural = u'Registro Beca de Primaria'

class RegistroBecaSecundariaInline(admin.TabularInline):
    model = RegistroBecaSecundaria
    extra = 1
    exclude = ('servicio_social', 'esp_propos', 'promotor', 'solidario_famila', 
               'solidario_centro','solidario_comunidad', 'solidario_sociedad')
    verbose_name_plural = u'Registro Beca de Secundaria'

class RegistroBecaUniversitariaInline(admin.TabularInline):
    model = RegistroBecaUniversitaria
    extra = 1
    exclude = ('servicio_social', 'esp_propos', 'promotor', 'solidario_famila', 
               'solidario_centro','solidario_comunidad', 'solidario_sociedad')
    verbose_name_plural = u'Registro Beca Universitaria'

# Inlines de registro en grupos musicales
class RegistroMusicaInline(admin.StackedInline):
    model = RegistroMusica
    extra = 1
    verbose_name_plural = u'Registro grupo de musica'

class RegistroTeatroInline(admin.StackedInline):
    model = RegistroTeatro
    extra = 1
    verbose_name_plural = u'Registro grupo de teatro'

class RegistroDanzaInline(admin.StackedInline):
    model = RegistroDanza
    extra = 1
    verbose_name_plural = u'Registro grupo de danza'

class RegistroCoroInline(admin.StackedInline):
    model = RegistroCoro
    extra = 1
    verbose_name_plural = u'Registro grupo de coro'

class RegistroPinturaInline(admin.StackedInline):
    model = RegistroPintura
    extra = 1
    verbose_name_plural = u'Registro grupo de pintura'

class PersonaAdmin(admin.ModelAdmin):
    add_form_template = 'admin/registro/add_form_template.html'
    fieldsets = [
        ('Datos personales', {'fields': [('primer_nombre', 'segundo_nombre'), ('primer_apellido', 'segundo_apellido'), 
                                        ('sexo', 'fecha_nacimiento'), ('codigo', 'cedula'), ('personal_ccbn', 'docente_ccbn')]}),
        ('Ubicacion', {'fields': [('municipio', 'ciudad'), ('barrio', 'distrito'), 'direccion', ('telefono', 'celular')]}),
        (u'Información Académica', {'fields': [('nivel_academico', 'nivel_estudio'), 'centro_actual']}),
        ('Datos del Hogar', {'fields': ['oficio', 'con_quien_vive', 'tipo_familia',]}),
        ('Jefe de Familia', {'fields': [('jefe_familia', 'j_oficio'), ('j_primer_nombre', 'j_segundo_nombre'), 
                                        ('j_primer_apellido', 'j_segundo_apellido')],})
                                                                                     
    ]

    inlines = [RelacionInline, ModuloPersonaInline, FormacionBasicaInline, FormacionVocacionalInline, FormacionArtisticaInline]

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    def response_add(self, request, obj):
        return super(PersonaAdmin, self).response_add(request, obj, '../%s/#laconcha')

    def add_view(self, request):
        self.inlines=[RelacionInline, ModuloPersonaInline]
        return super(PersonaAdmin, self).add_view(request)

    def change_view(self, request, obj_id):
        inlines = []
        self.inlines = [RelacionInline, ModuloPersonaInline]        
        try:
            modulos = Persona.objects.get(id=obj_id).modulopersona
            
            # agregando inlines del modulo biblioteca
            for obj in modulos.biblioteca.all().exclude(inline__exact=''):
                inlines.append(obj.inline)
            # agregando inlines del modulo de formacion        
            for obj in modulos.formacion.all().exclude(inline__exact=''):
                inlines.append(obj.inline)
            # agregando inlines del modulo de atencion integrals
            for obj in modulos.atencion_integral.all().exclude(inline__exact=''):
                inlines.append(obj.inline)
            # agregando inlines del modulo de promocion artistica
            for obj in modulos.promocion_artistica.all().exclude(inline__exact=''):
                inlines.append(obj.inline)

            self.inlines += [eval(inline) for inline in inlines]

        except Exception as e:
            
            print e

        return super(PersonaAdmin, self).change_view(request, obj_id)

    class Media:
        css = {
            'screen': ('/files/css/admin.css', '/files/js/chosen.css'),            
        }
        js= ['http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js', 
            '/files/js/chosen.jquery.min.js', '/files/js/admin.js']


admin.site.register(Persona, PersonaAdmin)
admin.site.register(Pariente)
admin.site.register(Relacion)
admin.site.register(Ciudad)
admin.site.register(Barrio)
admin.site.register(Oficio)