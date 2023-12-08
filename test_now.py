#!/usr/bin/env python3 
from models.base_model import BaseModel
from models import storage
from models.user import User

all_objs = storage.all()

print('------Reloaded Objects-------')
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-----Create a new User-------")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@gmail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print('-------------------------------')
print(my_user.email, my_user.password, my_user.first_name, my_user.last_name)
