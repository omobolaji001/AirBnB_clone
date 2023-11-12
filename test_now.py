#!/usr/bin/env python3 
from models.base_model import BaseModel
import models

model = BaseModel()
obj = models.storage.all().values()
for ob in obj:
    print(ob)

print('-------------')
print(model)
