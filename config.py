import os

class Config:
  SECRET_KEY = os.envirorn.get('SECRET_KEY') or 'this-aint-none-of-your-business'