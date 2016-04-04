# coding: utf-8

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Centros(models.Model):
    idcentro = models.CharField(max_length=765, db_column='IdCentro') # Field name made lowercase.
    centro = models.CharField(max_length=765, db_column='Centro', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=765, db_column='Nombre', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Centros'

class Contratos(models.Model):
    investigador = models.CharField(max_length=750, db_column='Investigador', blank=True) # Field name made lowercase.
    dni = models.CharField(max_length=765, db_column='DNI', blank=True) # Field name made lowercase.
    centro = models.CharField(max_length=765, db_column='Centro', blank=True) # Field name made lowercase.
    institucion = models.CharField(max_length=750, db_column='Institucion', blank=True) # Field name made lowercase.
    fecha = models.IntegerField(null=True, db_column='A\xc3\xb1o', blank=True) # Field name made lowercase. año -> fecha
    class Meta:
        db_table = u'Contratos'

class Coordinadoresareas(models.Model):
    idarea = models.IntegerField(null=True, db_column='IdArea', blank=True) # Field name made lowercase.
    area = models.CharField(max_length=765, db_column='Area', blank=True) # Field name made lowercase.
    dni = models.CharField(max_length=765, db_column='DNI', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=765, db_column='Nombre', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CoordinadoresAreas'

class Coordinadoresgrupos(models.Model):
    idseccion = models.CharField(max_length=765, db_column='iDSeccion', blank=True) # Field name made lowercase.
    seccion = models.CharField(max_length=765, db_column='Seccion', blank=True) # Field name made lowercase.
    ip = models.CharField(max_length=765, db_column='IP', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CoordinadoresGrupos'

class Grupos(models.Model):
    #id = models.IntegerField(db_column='Id') # Field name made lowercase.
    idseccion = models.CharField(max_length=765, db_column='IdSeccion', blank=True) # Field name made lowercase.
    codigo = models.CharField(max_length=765, db_column='Codigo', blank=True) # Field name made lowercase.
    seccion = models.CharField(max_length=765, db_column='Seccion', blank=True) # Field name made lowercase.
    area = models.CharField(max_length=765, db_column='Area', blank=True) # Field name made lowercase.
    tipo = models.CharField(max_length=765, db_column='Tipo', blank=True) # Field name made lowercase.
    sistema = models.CharField(max_length=765, db_column='Sistema', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Grupos'

class Institucionespublicaciones(models.Model):
    ute = models.CharField(max_length=150, db_column='UTE') # Field name made lowercase.
    instituciones = models.TextField(db_column='Instituciones', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'InstitucionesPublicaciones'

class Investigadores(models.Model):
    #id = models.IntegerField(db_column='Id') # Field name made lowercase.
    dni = models.CharField(max_length=765, db_column='DNI', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=765, db_column='Nombre', blank=True) # Field name made lowercase.
    nombrecompleto = models.CharField(max_length=765, db_column='NombreCompleto', blank=True) # Field name made lowercase.
    primerapellido = models.CharField(max_length=765, db_column='PrimerApellido', blank=True) # Field name made lowercase.
    segundoapellido = models.CharField(max_length=765, db_column='SegundoApellido', blank=True) # Field name made lowercase.
    investigador = models.CharField(max_length=765, db_column='Investigador', blank=True) # Field name made lowercase.
    campo7 = models.CharField(max_length=765, db_column='Campo7', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Investigadores'

class Investigadoresgrupos(models.Model):
    investigador = models.CharField(max_length=750, db_column='Investigador', blank=True) # Field name made lowercase.
    dni = models.CharField(max_length=765, db_column='DNI', blank=True) # Field name made lowercase.
    idseccion = models.CharField(max_length=150, db_column='IdSeccion', blank=True) # Field name made lowercase.
    seccion = models.CharField(max_length=750, db_column='Seccion', blank=True) # Field name made lowercase.
    fecha = models.IntegerField(null=True, db_column='A\xc3\xb1o', blank=True) # Field name made lowercase. año -> fecha
    class Meta:
        db_table = u'InvestigadoresGrupos'

class Investigadorespublicaciones(models.Model):
    dni = models.CharField(max_length=765, db_column='DNI', blank=True) # Field name made lowercase.
    nombrecompleto = models.CharField(max_length=765, db_column='NombreCompleto', blank=True) # Field name made lowercase.
    idinvestigador = models.CharField(max_length=765, db_column='IdInvestigador', blank=True) # Field name made lowercase.
    idprodrevistas = models.IntegerField(null=True, db_column='IdProdrevistas', blank=True) # Field name made lowercase.
    firma = models.CharField(max_length=150, db_column='Firma', blank=True) # Field name made lowercase.
    centro = models.CharField(max_length=765, db_column='Centro', blank=True) # Field name made lowercase.
    idseccion = models.CharField(max_length=150, db_column='IdSeccion', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'InvestigadoresPublicaciones'

class Publicaciones(models.Model):
    idprorevistas = models.IntegerField(null=True, db_column='IdProrevistas', blank=True) # Field name made lowercase.
    autores = models.TextField(db_column='Autores', blank=True) # Field name made lowercase.
    instituciones_1 = models.TextField(db_column='Instituciones_1', blank=True) # Field name made lowercase.
    instituciones = models.TextField(db_column='Instituciones', blank=True) # Field name made lowercase.
    titulo = models.TextField(db_column='Titulo', blank=True) # Field name made lowercase.
    revista = models.CharField(max_length=765, db_column='Revista', blank=True) # Field name made lowercase.
    fechapub = models.FloatField(null=True, db_column='A\xc3\xb1opub', blank=True) # Field name made lowercase. añopub -> fechapub
    volumen = models.CharField(max_length=150, db_column='Volumen', blank=True) # Field name made lowercase.
    numero = models.CharField(max_length=150, db_column='Numero', blank=True) # Field name made lowercase.
    paginas = models.CharField(max_length=765, db_column='Paginas', blank=True) # Field name made lowercase.
    tipodoc = models.CharField(max_length=765, db_column='Tipodoc', blank=True) # Field name made lowercase.
    idioma = models.CharField(max_length=765, db_column='Idioma', blank=True) # Field name made lowercase.
    citas = models.FloatField(null=True, db_column='Citas', blank=True) # Field name made lowercase.
    issnstandar = models.CharField(max_length=765, db_column='ISSNStandar', blank=True) # Field name made lowercase.
    issnplus = models.CharField(max_length=765, db_column='ISSNPlus', blank=True) # Field name made lowercase.
    isbn = models.CharField(max_length=150, db_column='ISBN', blank=True) # Field name made lowercase.
    basededatos = models.CharField(max_length=765, db_column='Basededatos', blank=True) # Field name made lowercase.
    ute = models.CharField(max_length=150, db_column='UTE', blank=True) # Field name made lowercase.
    doi = models.CharField(max_length=450, db_column='DOI', blank=True) # Field name made lowercase.
    funding_wos1 = models.TextField(db_column='Funding Wos1', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    funding_wos2 = models.TextField(db_column='Funding Wos2', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    pubmedid_sc = models.CharField(max_length=150, db_column='PUBMEDID SC', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    keyword1 = models.TextField(db_column='Keyword1', blank=True) # Field name made lowercase.
    keyword2 = models.TextField(db_column='Keyword2', blank=True) # Field name made lowercase.
    disciplinaisi = models.TextField(db_column='DisciplinaISI', blank=True) # Field name made lowercase.
    keywordisi1 = models.TextField(db_column='KeywordISI1', blank=True) # Field name made lowercase.
    keywordisi2 = models.TextField(db_column='KeywordISI2', blank=True) # Field name made lowercase.
    abstract = models.TextField(db_column='Abstract', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Publicaciones'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(unique=True, max_length=250)
    model = models.CharField(unique=True, max_length=250)
    class Meta:
        db_table = u'django_content_type'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=240)
    class Meta:
        db_table = u'auth_group'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type = models.ForeignKey(DjangoContentType)
    codename = models.CharField(unique=True, max_length=250)
    class Meta:
        db_table = u'auth_permission'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=90)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey(DjangoContentType, null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class ViewProductionRanking(models.Model):
    idprorevistas = models.IntegerField(null=True, db_column='IdProRevistas', blank=True) # Field name made lowercase.
    titulo = models.CharField(max_length=765, db_column='Titulo', blank=True) # Field name made lowercase.
    autores = models.CharField(max_length=765, db_column='Autores', blank=True) # Field name made lowercase.
    investigador = models.CharField(max_length=765, db_column='Investigador', blank=True) # Field name made lowercase.
    centro = models.CharField(max_length=765, db_column='Centro', blank=True) # Field name made lowercase.
    hospitalario = models.IntegerField(null=True, db_column='Hospitalario', blank=True) # Field name made lowercase.
    cuartil = models.CharField(max_length=765, db_column='Cuartil', blank=True) # Field name made lowercase.
    decil = models.IntegerField(null=True, db_column='Decil', blank=True) # Field name made lowercase.
    top3 = models.IntegerField(null=True, db_column='Top3', blank=True) # Field name made lowercase.
    area = models.CharField(max_length=765, db_column='Area', blank=True) # Field name made lowercase.
    grupo = models.CharField(max_length=765, db_column='Grupo', blank=True) # Field name made lowercase.
    fechapub = models.FloatField(null=True, db_column='A\xc3\xb1opub', blank=True) # Field name made lowercase. añopub -> fechapub
    issnplus = models.CharField(max_length=765, db_column='ISSNPlus', blank=True) # Field name made lowercase.
    revista = models.CharField(max_length=765, db_column='Revista', blank=True) # Field name made lowercase.
    idcategoriaisi = models.CharField(max_length=765, db_column='IdCategoriaISI', blank=True) # Field name made lowercase.
    impact = models.FloatField(null=True, db_column='Impact', blank=True) # Field name made lowercase.
    impact5 = models.FloatField(null=True, db_column='5Impact', blank=True) # Field name made lowercase. 5impact -> impact5
    citas = models.FloatField(null=True, db_column='Citas', blank=True) # Field name made lowercase.
    categoriaisi = models.CharField(max_length=765, db_column='CategoriaISI', blank=True) # Field name made lowercase.
    ute = models.CharField(max_length=765, db_column='UTE', blank=True) # Field name made lowercase.
    instituciones = models.TextField(db_column='Instituciones', blank=True) # Field name made lowercase.
    asistencial = models.CharField(max_length=765, db_column='Asistencial', blank=True) # Field name made lowercase.
    publico = models.CharField(max_length=765, db_column='Publico', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_production_ranking'

