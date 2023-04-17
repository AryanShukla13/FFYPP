from import_export import resources
from .models import Person

class SessionalResource(resources.ModelResource):
    class meta:
        model = 