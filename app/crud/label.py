from app.models import Label
from app.schemas.label import LabelCreate, LabelUpdate

from .base import CRUDBase


class CRUDLabel(CRUDBase[Label, LabelCreate, LabelUpdate]):
    pass


label = CRUDLabel(Label)
