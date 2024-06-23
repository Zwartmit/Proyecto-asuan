from django.db import models

class Categoria (models.Model):
    categoria = models.CharField(max_length=50, verbose_name="Categoria", unique=True)

    def __str__(self):
        return f"\nCategoria: {self.categoria}\n\n"

    class Meta:
        verbose_name= "categoria"
        verbose_name_plural ='categorias'
        db_table ='Categoria'
    
########################################################################################################################################
    

class Marca (models.Model):
    marca = models.CharField(max_length=50, verbose_name="Marca", unique=True)

    def __str__(self):
        return f"\nMarca: {self.marca}\n\n"

    class Meta:
        verbose_name= "marca"
        verbose_name_plural ='marcas'
        db_table ='Marca'
        
########################################################################################################################################

class Presentacion (models.Model):
    presentacion = models.CharField(max_length=50, verbose_name="Presentacion", unique=True)

    def __str__(self):
        return f"\nPresentación: {self.presentacion}\n\n"

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
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    id_presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"\nProducto: {self.producto}\nCantidad: {self.cantidad}\nValor: {self.valor}\nEstado: {self.estado}\n\n"

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

    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveIntegerField(verbose_name="Numero de documento", unique=True)
    email = models.EmailField(max_length=50, verbose_name="Email")
    telefono = models.PositiveIntegerField(verbose_name="Telefono")

    def __str__(self):
        return f"\nNombre: {self.nombre}\nTipo de documento: {self.tipo_documento}\nNúmero de documento: {self.numero_documento}\nEmail: {self.email}\nTeléfono: {self.telefono}\n\n"

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

    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveIntegerField(verbose_name="Numero de documento", unique=True)
    email = models.EmailField(max_length=50, verbose_name="Email")
    telefono = models.PositiveIntegerField(verbose_name="Telefono")

    def __str__(self):
        return f"\nNombre: {self.nombre}\nTipo de documento: {self.tipo_documento}\nNúmero de documento: {self.numero_documento}\nEmail: {self.email}\nTeléfono: {self.telefono}\n\n"
    
    class Meta:
        verbose_name= "cliente"
        verbose_name_plural ='clientes'
        db_table ='Cliente'

########################################################################################################################################

class Plato(models.Model):
    nombre_plato = models.CharField(max_length=50, verbose_name="Nombre_plato")
    descripcion = models.CharField(max_length=300, verbose_name="Descripcion")
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    def __str__(self):
        return f"\nPlato: {self.nombre_plato}\n Descripción: {self.descripcion},\nValor: {self.valor}\nEstado: {self.estado}\n\n"

    class Meta:
        verbose_name= "plato"
        verbose_name_plural ='platos'
        db_table ='Plato'

########################################################################################################################################

class Cuenta(models.Model):
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Subtotal")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_mesero = models.ForeignKey(Mesero, on_delete=models.CASCADE)
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

    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveIntegerField(verbose_name="Numero de documento", unique=True)
    email = models.EmailField(max_length=50, verbose_name="Email")
    telefono = models.PositiveIntegerField(verbose_name="Telefono")
    contraseña = models.CharField(max_length=50,verbose_name="Contraseña")

    def __str__(self):
        return f"\nNombre: {self.nombre}\nTipo de documento: {self.tipo_documento}\nNúmero de documento: {self.numero_documento}\nEmail: {self.email}\nTeléfono: {self.telefono}\nContraseña: {self.contraseña}\n\n"

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
        
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveIntegerField(verbose_name="Numero de documento", unique=True)
    email = models.EmailField(max_length=50, verbose_name="Email")
    telefono = models.PositiveIntegerField(verbose_name="Telefono")
    contraseña = models.CharField(max_length=50,verbose_name="Contraseña")

    def __str__(self):
        return f"\nNombre: {self.nombre}\nTipo de documento: {self.tipo_documento}\nNúmero de documento: {self.numero_documento}\nEmail: {self.email}\nTeléfono: {self.telefono}\nContraseña: {self.contraseña}\n\n"

    class Meta:
        verbose_name= "operador"
        verbose_name_plural ='operadores'
        db_table ='Operador'

########################################################################################################################################

class Venta(models.Model):
    cantidad_producto = models.PositiveIntegerField(verbose_name="Cantidad_producto")
    total_venta = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Total_venta")
    total_venta_iva = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Total_venta_iva")
    fecha_venta = models.DateTimeField(null=False, blank=True, verbose_name="Fecha_venta")
    id_admin = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    id_operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    id_cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    id_producto = models.ManyToManyField(Producto)

    def __str__(self):
        return f"\nCantidad producto: {self.cantidad_producto}\n Total venta: {self.total_venta}\nTotal venta IVA: {self.total_venta_iva}\nFecha venta: {self.fecha_venta}\n\n"

    class Meta:
        verbose_name= "venta"
        verbose_name_plural ='ventas'
        db_table ='Venta'

########################################################################################################################################        

class Metodo_pago(models.Model):
    
    class MetodoPago(models.TextChoices):
        EF = 'EF', 'Efectivo'
        TF = 'TF', 'Transferencia'
    metodo = models.CharField(max_length=2, choices=MetodoPago.choices, default=MetodoPago.EF, verbose_name="Metodo")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    def __str__(self):
        return f"\nMetodo: {self.metodo}\nEstado: {self.estado}\n\n"

    class Meta:
        verbose_name= "metodo_pago"
        verbose_name_plural ='metodos_pago'
        db_table ='Metodo_pago'

########################################################################################################################################

class Factura(models.Model):
    fecha_emision_factura = models.DateTimeField(null=False, blank=True, verbose_name="Fecha_emision_factura")
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_metodo = models.ForeignKey(Metodo_pago, on_delete=models.CASCADE)

    def __str__(self):
        return f"\nFecha de emisión factura: {self.fecha_emision_factura}\n\n"

    class Meta:
        verbose_name= "factura"
        verbose_name_plural ='facturas'
        db_table ='Factura'

########################################################################################################################################
