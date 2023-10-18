from django.db import models


class Sector(models.Model):
    id = models.BigAutoField(primary_key=True)
    sector = models.CharField(verbose_name="Sector", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sectores"
        verbose_name = "Sector"
        verbose_name_plural = "Sectores"
        ordering = ["sector"]
        
    def save(self, force_insert=False, force_update=False):
        self.sector = self.sector.upper()
        self.descripcion = self.descripcion.upper()
        super(Sector, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.sector)



class Ramo(models.Model):
    id = models.BigAutoField(primary_key=True)
    ramo = models.CharField(verbose_name="Ramo", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, default=0, verbose_name="Sector")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "ramos"
        verbose_name = "Ramo"
        verbose_name_plural = "Ramos"
        ordering = ["ramo"]
        
    def save(self, force_insert=False, force_update=False):
        self.ramo = self.ramo.upper()
        self.descripcion = self.descripcion.upper()
        super(Ramo, self).save(force_insert, force_update)

    def __str__(self):
        return "%s - %s" % (self.ramo, self.sector)


class Actividad(models.Model):
    id = models.BigAutoField(primary_key=True)
    actividad = models.CharField(
        verbose_name="Nombre de la actividad", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    ramo = models.ForeignKey(Ramo, on_delete=models.PROTECT, default=0, verbose_name="Ramo")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "actividades"
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["actividad"]
        
    def save(self, force_insert=False, force_update=False):
        self.actividad = self.actividad.upper()
        self.descripcion = self.descripcion.upper()
        super(Actividad, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.actividad)
    

class Segmento(models.Model):
    segmento = models.CharField('Segmento', max_length=50, null=False, blank=False)
    descripcion = models.TextField("Descripción")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "segmentos"
        verbose_name = "Segmento"
        verbose_name_plural = "Segmentos"
        ordering = ["segmento"]
        
    def save(self, force_insert=False, force_update=False):
        self.segmento = self.segmento.upper()
        self.descripcion = self.descripcion.upper()
        super(Segmento, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.segmento)
    

class Pais(models.Model):
    id = models.BigAutoField(primary_key=True)
    pais = models.CharField(
        verbose_name="Nombre", max_length=50, null=False, blank=False)
    iso = models.CharField(max_length=2, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "paises"
        verbose_name = "País"
        verbose_name_plural = "Países"
        ordering = ["pais"]
        
    def save(self, force_insert=False, force_update=False):
        self.pais = self.pais.upper()
        self.iso = self.iso.upper()
        super(Pais, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.pais)


class Estado(models.Model):
    id = models.BigAutoField(primary_key=True)
    estado = models.CharField(
        verbose_name="Nombre", max_length=50, null=False, blank=False)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, default=0, verbose_name="País")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "estados"
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ["estado", "pais"]
        
    def save(self, force_insert=False, force_update=False):
        self.estado = self.estado.upper()
        super(Estado, self).save(force_insert, force_update)

    def __str__(self):
        return"%s" % (self.estado)

    
class Ciudad(models.Model):
    id = models.BigAutoField(primary_key=True)
    ciudad = models.CharField(verbose_name="Nombre", max_length=50, null=False, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, verbose_name="Estado")
    created_at = models.DateTimeField("Creado", auto_now=True)
    updated_at = models.DateTimeField("Actualizado", auto_now_add=True)

    class Meta:
        db_table = "ciudades"
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ["ciudad", "estado"]
        
    def save(self, force_insert=False, force_update=False):
        self.ciudad = self.ciudad.upper()
        super(Ciudad, self).save(force_insert, force_update)

    def __str__(self):
        return "%s %s" % (self.ciudad, self.estado)
    
    @property
    def pais(self):
        pais = self.estado.pais
        return pais


class Region(models.Model):
    id = models.BigAutoField(primary_key=True)
    region = models.CharField(verbose_name="Región", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "regiones"
        verbose_name = "Región"
        verbose_name_plural = "Regiones"
        ordering = ["region"]
        
    def save(self, force_insert=False, force_update=False):
        self.region = self.region.upper()
        self.descripcion = self.descripcion.upper()
        super(Region, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.region)



class TipoCapital(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo_capital = models.CharField(verbose_name="Tipo de capital", max_length=60, null=False, blank=False)
    descripcion = models.CharField(verbose_name="Descripción", max_length=120)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tipocapitales"
        verbose_name = "Tipo de capital"
        verbose_name_plural = "Tiptipo_capitalos de capital"
        ordering = ["tipo_capital"]
        
    def save(self, force_insert=False, force_update=False):
        self.tipo_capital = self.tipo_capital.upper()
        self.descripcion = self.descripcion.upper()
        super(TipoCapital, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.tipo_capital)


class Vendedor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Nombre", max_length=50, null=False, blank=False)
    apellido = models.CharField(
        verbose_name="Apellido", max_length=50, null=False, blank=False)
    cedula = models.CharField(verbose_name="Nº de Cédula", max_length=12, null=False, blank=False)
    numero_fiscal = models.CharField(verbose_name="RIF", max_length=10, null=False, blank=False)
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
        self.numero_fiscal = self.numero_fiscal.upper()
        self.direccion = self.direccion.upper()
        super(Vendedor, self).save(force_insert, force_update)

    def __str__(self):
        return "%s, %s" % (self.apellido, self.nombre)


class Zona(models.Model):
    id = models.BigAutoField(primary_key=True)
    zona = models.CharField(verbose_name="Zona", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name="Región")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "zonas"
        verbose_name = "Zona"
        verbose_name_plural = "Zonas"
        ordering = ["region", "zona"]
        
    def save(self, force_insert=False, force_update=False):
        self.zona = self.zona.upper()
        self.descripcion = self.descripcion.upper()
        super(Zona, self).save(force_insert, force_update)

    def __str__(self):
        return "%s - %s" % (self.zona, self.region)


class TamanoEmpresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    tamano_empresa = models.CharField(verbose_name="Tamaño de empresa", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tamano_empresa"
        verbose_name = "Tamaño de empresa"
        verbose_name_plural = "Tamaños de empresa"
        ordering = ["tamano_empresa"]
        
    def save(self, force_insert=False, force_update=False):
        self.tamano_empresa = self.tamano_empresa.upper()
        self.descripcion = self.descripcion.upper()
        super(TamanoEmpresa, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.tamano_empresa)


class TipoEmpresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo_empresa = models.CharField(verbose_name="Tipo de empresa", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tipo_empresa"
        verbose_name = "Tipo de empresa"
        verbose_name_plural = "Tipos de empresa"
        ordering = ["tipo_empresa"]
        
    def save(self, force_insert=False, force_update=False):
        self.tipo_empresa = self.tipo_empresa.upper()
        self.descripcion = self.descripcion.upper()
        super(TipoEmpresa, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.tipo_empresa)
