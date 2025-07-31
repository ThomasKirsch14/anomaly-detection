import torch
import cv2
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd
from duetwebapi import DuetWebAPI as DWA
import json
from glob import glob


from functions import adjust_code, resize_with_padding, get_printer

model = torch.hub.load('yolov5', 'custom', path='model.onnx', source='local', force_reload=True, verbose=False)


printer, sfactor, efactor, temp = get_printer('192.0.2.1')



"""
values = pd.read_csv('printer.csv')
val = pd.DataFrame(values)
val.head()
sfactor = val['sfactor'][0] 
efactor = val['efactor'][0] 
temp = val['temp'][0] """



files = glob('test_images/*.jpg')
collection = []
for i, file in enumerate(files):
    im = cv2.imread(file)
    im = resize_with_padding(im, 640)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    result = model(im)
    df = result.pandas().xyxy[0][['confidence', 'class', 'name']]
    df['filename'] = file
    #cv2.imwrite(f'detection_{i}.jpg', np.squeeze(result.render()))
    collection.append(df)
    final = pd.concat(collection, ignore_index=True)
    final = final[final['confidence'] >= 0.369]

labels = final['name'].tolist()
conf = final['confidence'].tolist()

sf, ef, t = adjust_code(labels, sfactor, efactor, temp)

printer.send_code(f'M221 S{ef}')
printer.send_code(f'M104 S{t}')
printer.send_code(f'M220 S{sf}')


"""val.loc[0, 'sfactor'] = sf
val.loc[0, 'efactor'] = ef
val.loc[0, 'temp'] = t"""
