#!/usr/bin/env python3

from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded Objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Created Objects --")
my_model = BaseModel()
my_model.name = "First Model"
my_model.number = 77
my_model.save()
print(my_model)
