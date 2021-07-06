from django.contrib import admin

from .models import Dong
from .models import SearchKeyword

# Register your models here.
admin.site.register(Dong)
admin.site.register(SearchKeyword)