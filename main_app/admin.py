from django.contrib import admin
# import your models here
from .models import Dog, Toy, Feeding
# from .models import Toy

# Register your models here.
admin.site.register(Dog)
admin.site.register(Toy)
admin.site.register(Feeding)
