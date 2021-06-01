from app import ma
from app.models.headlinesmodel import HeadlineModel

class AreaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HeadlineModel
        load_instance = True
        load_only = ("store",)
        include_fk = True