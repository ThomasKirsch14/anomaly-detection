import torch
import cv2
import numpy as np
import pandas as pd
from pathlib import Path
from glob import glob
import os

# Modell laden
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/gpu100-2/weights/best.pt', force_reload=True)
# Model Parameter einstellen:
model.conf = 0.7
model.iou = 0.45
model.max_det = 2

# G-Code Modifikation
def adjust_gcode(temperature=None, speed=None, exfac=None):
    if temperature:
        print(f"Adjusting temperature by {temperature}°C")
        #print(printer.send_code('G28 X'))
    if speed:
        print(f"Adjusting speed to {speed} mm/s")
    if exfac:
        print(f'Extrusion factor adjusted: {exfac}%')

input_folder = 'E:/coding/model_testing/'
output_folder = 'E:/coding/model_testing/output/'

# Sicherstellen, dass das Ausgabe-Verzeichnis existiert
Path(output_folder).mkdir(parents=True, exist_ok=True)

# Bild-Dateien im Eingangsordner finden
image_paths = glob(os.path.join(input_folder, '*'))

for image in image_paths:
    if os.path.isfile(image):
        img = cv2.imread(image)

        # Überprüfe, ob das Bild erfolgreich geladen wurde
        if img is None:
            print(f"Bild {image} konnte nicht geladen werden.")
            continue

        results = model(img)
        df = results.pandas().xyxy[0]

        defect = None
        for j, row in df.iterrows():
            defect = row['name']
            confidence = round(row['confidence'], 2)
        if defect is not None:
            if 'stringing' in defect:
                adjust_gcode(temperature=200)
            if 'overextrusion' in defect:
                adjust_gcode(exfac=100)
            if 'stringing' in defect and 'overextrusion' in defect:
                adjust_gcode(temperature=200, speed=60, exfac=100)

            render = results.render()[0]

            # Erstelle den vollständigen Pfad für die Ausgabedatei
            output_path = os.path.join(output_folder, f'result-{os.path.basename(image)}')

            # Debug-Ausgabe des Pfads
            print(f"Speichere Bild unter: {output_path}")

            # Speichern des bearbeiteten Bildes
            cv2.imwrite(output_path, render)

print("Bildverarbeitung abgeschlossen und G-Code modifiziert!")
