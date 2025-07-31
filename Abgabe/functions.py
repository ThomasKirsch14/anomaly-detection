import pandas as pd
import numpy as np
import cv2
from glob import glob
import json
from duetwebapi import DuetWebAPI as DWA



def adjust_code(labels, sfactor, efactor, temp):

    # Überprüfe auf Stringing und passe den Geschwindigkeitsfaktor (sfactor) und Temperatur (temp) an
    if 'stringing' in labels:
        print('Stringing erkannt! Passe die Parameter an.')

        if temp > 195:
            temp -= 10
            print(f'Extrusionstemperatur auf {temp}°C reduziert')
        else:
            print(f'Temperatur auf ein Minimum reduziert! ({temp}°C)')

        if sfactor > 80.0:
            sfactor -= 5
            print(f'Geschwindigkeitsfaktor auf {sfactor}% reduziert.')
            
        else:
            print(f'Speedfaktor auf ein Minimum reduziert! ({sfactor}%)')

    
    # Überprüfe auf Overextrusion und passe den Extrusionsfaktor (efactor) an
    if 'overextrusion' in labels:
        print('Overextrusion erkannt! Passe die Parameter an.')
        if efactor > 95.0:
            efactor -= 5
            print(f'Extrusionsfaktor auf {efactor}% reduziert.')
            print(f'printer.send(M221 S{efactor})')  # Sende den neuen Extrusionsfaktor
        else:
            print(f'Extrusionsfaktor auf Minimum! ({efactor}%)')

    # Rückgabe der aktualisierten Werte
    return sfactor, efactor, temp



def resize_with_padding(img_pil, target_size):
    h, w = img_pil.shape[:2]
    scale = target_size / max(h, w)
    new_w = int(w * scale)
    new_h = int(h * scale)

    resized_img = cv2.resize(img_pil, (new_w, new_h), interpolation=cv2.INTER_LINEAR)

    padded_img = np.zeros((target_size, target_size, 3), dtype=np.uint8)

    top = (target_size - new_h) // 2
    left = (target_size - new_w) // 2
    padded_img[top:top + new_h, left:left + new_w] = resized_img

    return padded_img

print('funktionen geladen')



def get_printer(hostname):
    p = DWA(f'http://{hostname}')

    # gebe alle Informationen aus
    s = p.send_code('M408')
    status = s['response']

    data = json.loads(status)

    """
    tool: Extruder (0, 1)
    efactor: Extrusionsfaktor (%)
    sfactor: Speed-Factor (%)
    temp: Extrusionstemperatur (°C)
    babystep: Babystep (Distanz Bett<->Nozzle), (mm)
    """


    tool = int(data['tool'])
    efactor = data['efactor'][tool] 
    sfactor = data['sfactor']
    temp = data['active'][tool+1] 
    babystep = data['babystep']

    return p, efactor, sfactor, temp
