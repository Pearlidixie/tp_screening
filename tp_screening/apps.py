from django.apps import AppConfig
from django.conf import settings
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig


class AppConfig(AppConfig):
    name = 'tp_screening'
    verbose_name = 'TP Subject Screening'


if settings.APP_NAME == 'tp_screening':

    from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU

    class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
        country = 'botswana'
        definitions = {
            '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                                 slots=[100, 100, 100, 100, 100, 100, 100]),
            '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                                 slots=[100, 100, 100, 100, 100])}
