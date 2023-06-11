from django.db import models


class Sector(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Sector", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sectores"
        verbose_name = "Sector"
        verbose_name_plural = "Sectores"
        ordering = ["nombre"]
        
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.upper()
        super(Sector, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.nombre)



class Ramo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Ramo", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, default=0, verbose_name="Sector")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "ramos"
        verbose_name = "Ramo"
        verbose_name_plural = "Ramos"
        ordering = ["nombre"]
        
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.upper()
        super(Ramo, self).save(force_insert, force_update)

    def __str__(self):
        return "%s - %s" % (self.nombre, self.sector)


class Actividad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(
        verbose_name="Nombre de la actividad", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    ramo = models.ForeignKey(Ramo, on_delete=models.PROTECT, default=0, verbose_name="Ramo")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "actividades"
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["nombre"]
        
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.upper()
        super(Actividad, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.nombre)


class Pais(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(
        verbose_name="Nombre", max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "paises"
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        ordering = ["nombre"]
        
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(Pais, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.nombre)


class Estado(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(
        verbose_name="Nombre", max_length=50, null=False, blank=False)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, default=0, verbose_name="País")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "estados"
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ["nombre", "pais"]
        
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(Estado, self).save(force_insert, force_update)

    def __str__(self):
        return"%s" % (self.nombre)

    
class Ciudad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Nombre", max_length=50, null=False, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, verbose_name="Estado")
    created_at = models.DateTimeField("Creado", auto_now=True)
    updated_at = models.DateTimeField("Actualizado", auto_now_add=True)

    class Meta:
        db_table = "ciudades"
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ["nombre", "estado"]
        
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(Ciudad, self).save(force_insert, force_update)

    def __str__(self):
        return "%s %s" % (self.nombre, self.estado)
    
    @property
    def pais(self):
        pais = self.estado.pais
        return pais


class Region(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Región", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "regiones"
        verbose_name = "Región"
        verbose_name_plural = "Regiones"
        ordering = ["nombre"]
        
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.upper()
        super(Region, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.nombre)



class TipoCapital(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Tipo de capital", max_length=60, null=False, blank=False)
    descripcion = models.CharField(verbose_name="Descripción", max_length=120)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tipocapitales"
        verbose_name = "Tipo de capital"
        verbose_name_plural = "Tipos de capital"
        ordering = ["nombre"]
        
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.upper()
        super(TipoCapital, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.nombre)


class Vendedor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Nombre", max_length=50, null=False, blank=False)
    apellido = models.CharField(
        verbose_name="Apellido", max_length=50, null=False, blank=False)
    cedula = models.CharField(verbose_name="Nº de Cédula", max_length=12, null=False, blank=False)
    rif = models.CharField(verbose_name="RIF", max_length=10, null=False, blank=False)
    direccion = models.CharField(verbose_name="Dirección", max_length=150, null=False, blank=False)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, verbose_name="Ciudad")
    telefono = models.CharField(verbose_name="Teléfono(s)", max_length=50, null=False, blank=False)
    email = models.EmailField(verbose_name="Email", max_length=80, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "vendedores"
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        ordering = ["apellido", "nombre"]
    
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        self.cedula = self.cedula.upper()
        self.rif = self.rif.upper()
        self.direccion = self.direccion.upper()
        super(Vendedor, self).save(force_insert, force_update)

    def __str__(self):
        return "%s, %s" % (self.apellido, self.nombre)


class Zona(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Zona", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name="Región")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "zonas"
        verbose_name = "Zona"
        verbose_name_plural = "Zonas"
        ordering = ["region", "nombre"]
        
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.upper()
        super(Zona, self).save(force_insert, force_update)

    def __str__(self):
        return "%s - %s" % (self.region, self.nombre)


class TamanoEmpresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Tamaño de empresa", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tamano_empresa"
        verbose_name = "Tamaño de empresa"
        verbose_name_plural = "Tamaños de empresa"
        ordering = ["nombre"]
        
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.upper()
        super(TamanoEmpresa, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.nombre)


class TipoEmpresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Tipo de empresa", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tipo_empresa"
        verbose_name = "Tipo de empresa"
        verbose_name_plural = "Tipos de empresa"
        ordering = ["nombre"]
        
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.upper()
        super(TipoEmpresa, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.nombre)
