from app.config import ma
from app.models.sourcesmodel import SourceModel

class SourceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SourceModel
        load_instance = True
        load_only = ("store",)
        include_fk = True