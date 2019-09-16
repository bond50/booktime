from django.forms import inlineformset_factory
from . import widgets
from . import models

BasketLineFormSet = inlineformset_factory(models.Basket, models.BasketLine, fields=("quantity",), extra=0,
                                          widgets={"quantity": widgets.PlusMinusNumberInput()}, )
