
# Proyecto de Detección de Objetos con YOLOv5 y OpenCV

## Descripción

Este proyecto consiste en entrenar un modelo de detección de objetos utilizando YOLOv5 y posteriormente utilizarlo para realizar detecciones en tiempo real mediante OpenCV. La detección de objetos permite identificar y etiquetar elementos en imágenes o video en función de un modelo previamente entrenado.

---

## Requisitos

Antes de ejecutar el código, asegúrate de instalar las siguientes bibliotecas:

* `torch`: para trabajar con PyTorch y cargar el modelo YOLOv5.
* `opencv-python`: para manejar la captura y procesamiento de video.
* YOLOv5: Descargado desde el repositorio oficial de Ultralytics en GitHub.

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor" data-darkreader-inline-fill=""></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install torch torchvision opencv-python
</code></div></div></pre>

---

## Estructura del Código

El proyecto se divide en dos etapas principales: entrenamiento del modelo y detección en tiempo real.

### 1. Entrenamiento del Modelo

Este bloque de código entrena un modelo YOLOv5 utilizando el conjunto de datos `coco.yaml`. Aquí configuramos la resolución de imagen, el tamaño de lote, las épocas de entrenamiento, y la ubicación de los pesos base de YOLOv5 (`yolov5s.pt`).

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor" data-darkreader-inline-fill=""></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python">import os

os.chdir("D:/ESP_MACHINE_LEARNING/MACHINE_LEARNING 2/Encuentro_final/yolov5")
!python train.py --img 640 --batch 16 --epochs 25 --data coco.yaml --weights yolov5s.pt --cache
</code></div></div></pre>

* `--img 640`: establece el tamaño de imagen en 640x640 píxeles.
* `--batch 16`: configura el tamaño de lote en 16.
* `--epochs 25`: entrena el modelo durante 25 épocas.
* `--data coco.yaml`: define el conjunto de datos y las clases (COCO dataset).
* `--weights yolov5s.pt`: utiliza los pesos base de YOLOv5s.

---

### 2. Detección en Tiempo Real

El siguiente bloque se encarga de realizar detección en tiempo real utilizando el modelo YOLOv5 entrenado. Se captura el video de la cámara y se procesa cada cuadro para detectar y etiquetar objetos.

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor" data-darkreader-inline-fill=""></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python">import cv2
import torch

# Cargar el modelo YOLOv5 entrenado
model = torch.hub.load('ultralytics/yolov5', 'custom', path='D:/ESP_MACHINE_LEARNING/MACHINE_LEARNING 2/Encuentro_final/yolov5/yolov5s.pt')
model.eval()

# Captura de video en tiempo real
cap = cv2.VideoCapture(0)  # Usa la cámara predeterminada

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar la inferencia en el cuadro actual
    results = model(frame)
    pred = results.pred[0]

    # Filtrar las detecciones con una confianza mínima de 0.5
    for det in pred:
        confidence = det[4].item()
        if confidence >= 0.5:
            x1, y1, x2, y2 = det[:4].tolist()
            label = f'{results.names[int(det[5])]} {confidence:.2f}'

            # Dibujar la caja delimitadora y la etiqueta
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Mostrar el cuadro con las detecciones
    cv2.imshow('Detección de objetos', frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
</code></div></div></pre>

### Explicación del Código de Detección

1. **Carga del Modelo** :

* `torch.hub.load(...)` carga el modelo YOLOv5 desde el archivo de pesos entrenado `yolov5s.pt`.

1. **Captura de Video** :

* `cv2.VideoCapture(0)` inicia la captura de video de la cámara.

1. **Procesamiento de Cuadros** :

* Para cada cuadro de video, el modelo hace la inferencia y se obtienen las detecciones.

1. **Filtrado de Detecciones** :

* Se filtran las detecciones para incluir solo aquellas con confianza ≥ 0.5.

1. **Dibujo de Cajas y Etiquetas** :

* Se dibujan cajas delimitadoras alrededor de los objetos detectados y se muestran las etiquetas con el nombre de la clase y el nivel de confianza.

1. **Mostrar Video** :

* `cv2.imshow(...)` muestra el cuadro procesado con las detecciones en tiempo real.

1. **Salida del Bucle** :

* El bucle se cierra si se presiona la tecla `q`.
