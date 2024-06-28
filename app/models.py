from django.db import models
from .choices import codigos_telefonicos_paises
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class Categoria (models.Model):
    categoria = models.CharField(max_length=50, verbose_name="Categoría", unique=True)

    def __str__(self):
        return f"{self.categoria}"

    class Meta:
        verbose_name= "categoria"
        verbose_name_plural ='categorias'
        db_table ='Categoria'
    
########################################################################################################################################
    
class Marca (models.Model):
    marca = models.CharField(max_length=50, verbose_name="Marca", unique=True)

    def __str__(self):
        return f"{self.marca}"

    class Meta:
        verbose_name= "marca"
        verbose_name_plural ='marcas'
        db_table ='Marca'
        
########################################################################################################################################

class Presentacion (models.Model):
    presentacion = models.CharField(max_length=50, verbose_name="Presentación", unique=True)

    def __str__(self):
        return f"{self.presentacion}"

    class Meta:
        verbose_name= "presentacion"
        verbose_name_plural ='presentaciones'
        db_table ='Presentacion'
        
########################################################################################################################################

class Producto(models.Model):
    producto = models.CharField(max_length=50, verbose_name="Producto")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    id_categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name="Categoría")
    id_marca = models.ForeignKey(Marca, on_delete=models.PROTECT, verbose_name="Marca")
    id_presentacion = models.ForeignKey(Presentacion, on_delete=models.PROTECT, verbose_name="Presentación")

    def __str__(self):
        return f"{self.producto}"

    class Meta:
        verbose_name= "producto"
        verbose_name_plural ='productos'
        db_table ='Producto'

########################################################################################################################################

class Mesero(models.Model):
    class TipoDocumento(models.TextChoices):
        CC = 'CC', 'Cédula de Ciudadanía'
        TI = 'TI', 'Tarjeta de Identidad'
        CE = 'CE', 'Cédula de Extranjería'
        RC = 'RC', 'Registro Civil'
        PSP = 'PSP', 'Pasaporte'

    def validar_numero_documento(value):
        if value < 10000000 or value > 9999999999:
            raise ValidationError("El número de documento debe tener entre 8 y 10 dígitos")
        
    def validar_email(value):
        value = "foo.bar@baz.qux"
        try:
            validate_email(value)
        except ValidationError:
            raise ValidationError("Correo rechazado")  
        
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveIntegerField(verbose_name="Número de documento", unique=True, validators=[validar_numero_documento])
    email = models.EmailField(max_length=50, verbose_name="Email", validators=[validate_email])
    pais_telefono = models.CharField(max_length=50, choices=[(pais, pais) for pais in codigos_telefonicos_paises], default='Colombia (+57)', verbose_name="Prefijo telefónico")
    telefono = models.PositiveIntegerField(verbose_name="Teléfono")

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name= "mesero"
        verbose_name_plural ='meseros'
        db_table ='Mesero'

########################################################################################################################################

class Cliente(models.Model):
    class TipoDocumento(models.TextChoices):
        CC = 'CC', 'Cédula de Ciudadanía'
        TI = 'TI', 'Tarjeta de Identidad'
        CE = 'CE', 'Cédula de Extranjería'
        RC = 'RC', 'Registro Civil'
        PSP = 'PSP', 'Pasaporte'

    def validar_numero_documento(value):
        if value < 10000000 or value > 9999999999:
            raise ValidationError("El número de documento debe tener entre 8 y 10 dígitos")
        
    def validar_email(value):
        value = "foo.bar@baz.qux"
        try:
            validate_email(value)
        except ValidationError:
            raise ValidationError("Correo rechazado")  
        
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveIntegerField(verbose_name="Número de documento", unique=True, validators=[validar_numero_documento])
    email = models.EmailField(max_length=50, verbose_name="Email", validators=[validate_email])
    pais_telefono = models.CharField(max_length=50, choices=[(pais, pais) for pais in codigos_telefonicos_paises], default='Colombia (+57)', verbose_name="Prefijo telefónico")
    telefono = models.PositiveIntegerField(verbose_name="Teléfono")

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name= "cliente"
        verbose_name_plural ='clientes'
        db_table ='Cliente'

########################################################################################################################################

class Plato(models.Model):
    plato = models.CharField(max_length=50, verbose_name="Nombre del plato")
    descripcion = models.CharField(max_length=300, verbose_name="Descripción")
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    def __str__(self):
        return f"{self.plato}"

    class Meta:
        verbose_name= "plato"
        verbose_name_plural ='platos'
        db_table ='Plato'

########################################################################################################################################

class Cuenta(models.Model):
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Subtotal")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    id_mesero = models.ForeignKey(Mesero, on_delete=models.PROTECT)
    id_plato = models.ManyToManyField(Plato)

    def __str__(self):
        return f"\nCantidad: {self.cantidad},\nSubtotal: {self.subtotal}\n Estado: {self.estado}\n\n"

    class Meta:
        verbose_name= "cuenta"
        verbose_name_plural ='cuentas'
        db_table ='Cuenta'

########################################################################################################################################

class Administrador(models.Model):
    class TipoDocumento(models.TextChoices):
        CC = 'CC', 'Cédula de Ciudadanía'
        CE = 'CE', 'Cédula de Extranjería'
        PSP = 'PSP', 'Pasaporte'

    def validar_numero_documento(value):
        if value < 10000000 or value > 9999999999:
            raise ValidationError("El número de documento debe tener entre 8 y 10 dígitos\n")
        
    def validar_email(value):
        value = "foo.bar@baz.qux"
        try:
            validate_email(value)
        except ValidationError:
            raise ValidationError("Correo rechazado")  
    
    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get("numero_documento")
        if Administrador.objects.filter(numero_documento=numero_documento).exists():
            raise ValidationError("Ya hay un mesero registrado con este número de documento.")
        return numero_documento
        
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveIntegerField(verbose_name="Número de documento", unique=True, validators=[validar_numero_documento])
    email = models.EmailField(max_length=50, verbose_name="Email", validators=[validate_email])
    telefono = models.PositiveIntegerField(verbose_name="Teléfono")
    contraseña = models.CharField(max_length=50,verbose_name="Contraseña")
    conf_contraseña = models.CharField(max_length=50,verbose_name="Confirmación de contraseña", default="")

    def clean(self):
        super().clean()
        if self.contraseña != self.conf_contraseña:
            raise ValidationError({"conf_contraseña": "Las contraseñas no coinciden"})

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name= "administrador"
        verbose_name_plural ='administradores'
        db_table ='Administrador'

########################################################################################################################################

class Operador(models.Model):
    class TipoDocumento(models.TextChoices):
        CC = 'CC', 'Cédula de Ciudadanía'
        TI = 'TI', 'Tarjeta de Identidad'
        CE = 'CE', 'Cédula de Extranjería'
        PSP = 'PSP', 'Pasaporte'
        
    def validar_numero_documento(value):
        if value < 10000000 or value > 9999999999:
            raise ValidationError("El número de documento debe tener entre 8 y 10 dígitos")
        
    def validar_email(value):
        value = "foo.bar@baz.qux"
        try:
            validate_email(value)
        except ValidationError:
            raise ValidationError("Correo rechazado")  
        
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveIntegerField(verbose_name="Número de documento", unique=True, validators=[validar_numero_documento])
    email = models.EmailField(max_length=50, verbose_name="Email", validators=[validate_email])
    pais_telefono = models.CharField(max_length=50, choices=[(pais, pais) for pais in codigos_telefonicos_paises], default='Colombia (+57)', verbose_name="Prefijo telefónico")
    telefono = models.PositiveIntegerField(verbose_name="Teléfono")
    contraseña = models.CharField(max_length=50,verbose_name="Contraseña")

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name= "operador"
        verbose_name_plural ='operadores'
        db_table ='Operador'

########################################################################################################################################        

class Venta(models.Model):
    class MedotoPago(models.TextChoices):
        EF = 'EF', 'Efectivo'
        TF = 'TF', 'Transferencia'

    id_producto = models.ManyToManyField(Producto, verbose_name="Producto")
    cantidad_producto = models.PositiveIntegerField(verbose_name="Cantidad de productos")
    total_venta = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Total de la venta")
    total_venta_iva = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Total de la venta con iva")
    fecha_venta = models.DateTimeField(null=False, blank=True, verbose_name="Fecha de venta")
    metodo_pago = models.CharField(max_length=3, choices=MedotoPago.choices, default=MedotoPago.EF, verbose_name="Metodo de Pago")
    id_admin = models.ForeignKey(Administrador, on_delete=models.PROTECT, null=True, verbose_name="Administrador")
    id_operador = models.ForeignKey(Operador, on_delete=models.PROTECT, null=True, verbose_name="Operador")
    id_cuenta = models.ForeignKey(Cuenta, on_delete=models.PROTECT, verbose_name="Cuenta")

    def __str__(self):
        return f"\nCantidad producto: {self.cantidad_producto}\n Total venta: {self.total_venta}\nTotal venta IVA: {self.total_venta_iva}\nFecha venta: {self.fecha_venta}\n\n"

    class Meta:
        verbose_name= "venta"
        verbose_name_plural ='ventas'
        db_table ='Venta'

########################################################################################################################################

class Factura(models.Model):
    fecha_emision_factura = models.DateTimeField(null=False, blank=True, verbose_name="Fecha de emisión de la factura")
    id_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.fecha_emision_factura}"

    class Meta:
        verbose_name= "factura"
        verbose_name_plural ='facturas'
        db_table ='Factura'

########################################################################################################################################
