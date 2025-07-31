import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pylab as plt
import cv2
import os
import tkinter as tk
from tkinter import messagebox, filedialog

def select_output_dir(root_dir):
    root = tk.Tk()
    root.withdraw()
    output_dir = filedialog.askdirectory(title='directory to save image to:')
    root.destroy()

    return output_dir



# Koordinaten für den Bildausschnitt
"""x1, y1 = 600, 1000
x2, y2 = 2300, 2600"""

# Liste der Bilddateien
files = glob('./captures/*.png')

# Transformation für Schärfung
trafo = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

output_dir = select_output_dir()


if os.path.exists(output_dir) and os.listdir(output_dir):
    print(f'The output directory {output_dir} is not empty. Exiting the program.')
else:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

# Schleife über alle Dateien
for i, file in enumerate(files):
    img = cv2.imread(file)
    if img is None:
        print(f'Error in reading File {file}')

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (640, 640), interpolation=cv2.INTER_NEAREST)
    #sharpen = cv2.filter2D(img, -1, trafo)
    
    # Directories
    
    

    output_filename = os.path.basename(file)
    output_path = os.path.join(output_dir, output_filename)
    cv2.imwrite(output_path, img)
    
    print(f'cropped and processed image {i + 1} / {len(files)}\nsaved to {output_path}')
    
