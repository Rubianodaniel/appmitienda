from django.db import models
from django.contrib.auth.models import User


class Venta(models.Model):
    idventa = models.AutoField(db_column='idVenta', primary_key=True)  # Field name made lowercase.
    numeroventa = models.CharField(db_column='numeroVenta', max_length=6, blank=True, null=True)  # Field name made lowercase.
    idtipodocumentoventa = models.IntegerField(db_column='idTipoDocumentoVenta', blank=True, null=True)  # Field name made lowercase.
    idusuario = models.IntegerField(db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    documentocliente = models.CharField(db_column='documentoCliente', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nombrecliente = models.CharField(db_column='nombreCliente', max_length=20, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='subTotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impuestototal = models.DecimalField(db_column='impuestoTotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Venta'

class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    idrol = models.IntegerField(db_column='idRol', blank=True, null=True)  # Field name made lowercase.
    urlfoto = models.CharField(db_column='urlFoto', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nombrefoto = models.CharField(db_column='nombreFoto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    clave = models.CharField(max_length=100, blank=True, null=True)
    esactivo = models.TextField(db_column='esActivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'



class Tipodocumentoventa(models.Model):
    idtipodocumentoventa = models.AutoField(db_column='idTipoDocumentoVenta', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    esactivo = models.TextField(db_column='esActivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoDocumentoVenta'


class Rolmenu(models.Model):
    idrolmenu = models.AutoField(db_column='idRolMenu', primary_key=True)  # Field name made lowercase.
    idrol = models.IntegerField(db_column='idRol', blank=True, null=True)  # Field name made lowercase.
    idmenu = models.IntegerField(db_column='idMenu', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.TextField(db_column='esActivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RolMenu'


class Rol(models.Model):
    idrol = models.AutoField(db_column='idRol', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    esactivo = models.TextField(db_column='esActivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rol'


class Producto(models.Model):
    idproducto = models.AutoField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    codigobarra = models.CharField(db_column='codigoBarra', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    idcategoria = models.IntegerField(db_column='idCategoria', blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(blank=True, null=True)
    urlimagen = models.CharField(db_column='urlImagen', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nombreimagen = models.CharField(db_column='nombreImagen', max_length=100, blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    esactivo = models.TextField(db_column='esActivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Producto'


class Numerocorrelativo(models.Model):
    idnumerocorrelativo = models.AutoField(db_column='idNumeroCorrelativo', primary_key=True)  # Field name made lowercase.
    ultimonumero = models.IntegerField(db_column='ultimoNumero', blank=True, null=True)  # Field name made lowercase.
    cantidaddigitos = models.IntegerField(db_column='cantidadDigitos', blank=True, null=True)  # Field name made lowercase.
    gestion = models.CharField(max_length=100, blank=True, null=True)
    fechaactualizacion = models.DateTimeField(db_column='fechaActualizacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NumeroCorrelativo'


class Negocio(models.Model):
    idnegocio = models.IntegerField(db_column='idNegocio', primary_key=True)  # Field name made lowercase.
    urllogo = models.CharField(db_column='urlLogo', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nombrelogo = models.CharField(db_column='nombreLogo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    numerodocumento = models.CharField(db_column='numeroDocumento', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    porcentajeimpuesto = models.DecimalField(db_column='porcentajeImpuesto', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    simbolomoneda = models.CharField(db_column='simboloMoneda', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Negocio'


class Menu(models.Model):
    idmenu = models.AutoField(db_column='idMenu', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=30)
    idmenupadre = models.IntegerField(db_column='idMenuPadre', blank=True, null=True)  # Field name made lowercase.
    icono = models.CharField(max_length=30, blank=True, null=True)
    controlador = models.CharField(max_length=30, blank=True, null=True)
    paginaaccion = models.CharField(db_column='paginaAccion', max_length=30, blank=True, null=True)  # Field name made lowercase.
    esactivo = models.TextField(db_column='esActivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Menu'

class Detalleventa(models.Model):
    iddetalleventa = models.AutoField(db_column='idDetalleVenta', primary_key=True)  # Field name made lowercase.
    idventa = models.IntegerField(db_column='idVenta', blank=True, null=True)  # Field name made lowercase.
    idproducto = models.IntegerField(db_column='idProducto', blank=True, null=True)  # Field name made lowercase.
    marcaproducto = models.CharField(db_column='marcaProducto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descripcionproducto = models.CharField(db_column='descripcionProducto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categoriaproducto = models.CharField(db_column='categoriaProducto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DetalleVenta'




class Categoria(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    esactivo = models.TextField(db_column='esActivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categoria'


class Configuracion(models.Model):
    recurso = models.CharField(max_length=50, blank=True, null=True)
    propiedad = models.CharField(max_length=50, blank=True, null=True)
    valor = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Configuracion'































