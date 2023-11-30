from django.contrib import admin
from .models import Subject, Formation, Domaine, Emploi, Achat


admin.site.register(Subject)
admin.site.register(Formation)
admin.site.register(Domaine)
admin.site.register(Emploi)
admin.site.register(Achat)
