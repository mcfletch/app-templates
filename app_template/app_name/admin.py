try:
    from django.contrib import admin
except ImportError, err:
    admin = None 
else:
    from {{app_name}} import models 

#    class {{app_name}}Admin( admin.ModelAdmin ):
#        """Admin class"""
#    admin.site.register( models.{{app_name}}, {{app_name}}Admin )
