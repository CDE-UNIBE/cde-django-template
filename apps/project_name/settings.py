from .config.common import BaseSettings
from .config.mixins import DevMixin, ProdMixin, SecurityMixin


class DevConfig(DevMixin, BaseSettings):
    pass


class ProdConfig(ProdMixin, SecurityMixin, BaseSettings):
    pass
