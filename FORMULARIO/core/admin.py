from django.contrib import admin


from .models import Planta
from .models import Producto
from .models import ProduccionDiaria

admin.site.register(Planta)
admin.site.register(Producto)
admin.site.register(ProduccionDiaria)
# Register your models here.
