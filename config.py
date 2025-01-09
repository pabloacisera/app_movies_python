from decouple import config

class Config:
    SECRET_KEY=config('SECRET_KEY')

class DevConfig:
    DEBUG=True

config = {
    'dev': DevConfig
}
