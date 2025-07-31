# 🧠 Real-Time Process Monitoring in Additive Manufacturing Using ML

This project implements a real-time anomaly detection system for Fused Deposition Modeling (FDM), a common method in additive manufacturing (AM). Using a YOLOv5 model trained on a custom image dataset, the system detects and classifies process anomalies — specifically **stringing** and **over-extrusion** — as they occur during 3D printing.

> 🎓 This work was presented as part of a publication at the **CIRP CMS conference**

---

## 📌 Abstract

Additive manufacturing (AM) facilitates the production of complex, customized parts by building them up layer by layer, making it ideal for small batch production. However, the process is susceptible to defects and anomalies, particularly for low batch sizes, which can affect the quality of the final part.

This project proposes a **two-step framework** for real-time process monitoring and parameter adaptation:
1. **Anomaly detection and localization** using a computer vision model (YOLOv5)
2. **Adaptive adjustment** of printing parameters in response to the detected anomalies

The approach is validated through a case study on FDM (Fused Deposition Modeling) printing.

---

## 🧰 Technologies Used
### Tech Stack
- **YOLOv5** – Custom-trained object detection model
- **Python** – Data processing and model deployment
- **OpenCV** – Image acquisition and processing
- **PyTorch** – Deep learning framework for model training
- **MSVott** – Annotation tool for bounding box creation
### 3D-Printer
- Self-built 3D-Printer with Reprap Firmware and open architecture
- RaspberryPI4
- Logitech Webcam C920
---

## 📊 Features

- Real-time detection of **stringing** and **over-extrusion**
- Custom YOLOv5 training pipeline on domain-specific images
- Evaluation metrics (precision, recall, mAP)
- Visual overlay of predictions during live printing
- Extensible framework for additional defect classes

---

<div class="alert alert-info">

<i>This project is shared for demonstration purposes only and is not licensed for reuse.</i>

</div>



## 📘 Projektbeschreibung auf Deutsch

*Dieses Projekt wurde im Rahmen einer wissenschaftlichen Arbeit zur Echtzeit-Prozessüberwachung beim 3D-Druck (FDM) entwickelt. Ziel war es, ein ML-gestütztes Framework zu implementieren, um Anomalien während des Druckprozesses zu erkennen und durch Parameteranpassungen in situ einzudämmen. Die Lösung wurde eigenständig entwickelt und im Rahmen der CIRP CMS veröffentlicht.*

→ Für mehr Details siehe den englischen Abschnitt oben.


