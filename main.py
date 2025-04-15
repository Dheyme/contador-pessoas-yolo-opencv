# =============================================
# Contador de Pessoas com YOLOv8 + OpenCV
# Autor: [Seu Nome ou GitHub]
# Descrição: Este script utiliza o modelo YOLOv8 
# para detectar e contar pessoas entrando e saindo 
# de uma área definida em um vídeo.
# =============================================

import cv2
import numpy as np
from ultralytics import YOLO
import cvzone

# --------------------------------------------------
# Função de callback para capturar coordenadas do mouse
# Usada para definir áreas de entrada e saída manualmente
# --------------------------------------------------
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        point = [x, y]
        print(point)

# Criando janela e associando a função de callback
cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

# --------------------------------------------------
# Carregando o modelo YOLOv8 (versão pequena e leve)
# --------------------------------------------------
model = YOLO("yolo11n.pt")  # Certifique-se de ter o modelo na mesma pasta
names = model.names  # Mapeia os IDs para os nomes das classes

# --------------------------------------------------
# Abertura do vídeo (pode usar 0 para webcam)
# --------------------------------------------------
cap = cv2.VideoCapture('peoplecount1.mp4')

# Variáveis e estruturas para controle da lógica
count = 0
area1 = [(251, 443), (215, 447), (461, 577), (510, 570)]  # Área de entrada
area2 = [(201, 449), (177, 453), (403, 583), (448, 578)]  # Área de saída

enter = {}      # Dicionário para rastrear quem entrou
exit = {}       # Dicionário para rastrear quem saiu
list = []       # IDs únicos de entrada
list1 = []      # IDs únicos de saída

# --------------------------------------------------
# Loop principal para processar o vídeo frame a frame
# --------------------------------------------------
while True:
    ret, frame = cap.read()
    count += 1

    # Pula frames ímpares para reduzir carga computacional
    if count % 2 != 0:
        continue

    if not ret:
        break  # Encerra se não houver mais frames

    # Redimensiona o frame para manter padrão
    frame = cv2.resize(frame, (1020, 600))

    # Executa a detecção e rastreamento com YOLOv8
    results = model.track(frame, persist=True)

    # --------------------------------------------------
    # Processamento dos resultados da detecção
    # --------------------------------------------------
    if results[0].boxes is not None and results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.int().cpu().tolist()     # Caixas delimitadoras
        class_ids = results[0].boxes.cls.int().cpu().tolist()  # IDs das classes
        track_ids = results[0].boxes.id.int().cpu().tolist()   # IDs de rastreamento
        confidences = results[0].boxes.conf.cpu().tolist()     # Confiabilidade

        for box, class_id, track_id, conf in zip(boxes, class_ids, track_ids, confidences):
            c = names[class_id]
            
            # Verifica se o objeto detectado é uma pessoa
            if 'person' in c:
                x1, y1, x2, y2 = box

                #### VERIFICAÇÃO DE ENTRADA ####
                result = cv2.pointPolygonTest(np.array(area2, np.int32), ((x1, y2)), False)
                if result >= 0:
                    enter[track_id] = (x1, y2)

                if track_id in enter:
                    result1 = cv2.pointPolygonTest(np.array(area1, np.int32), ((x1, y2)), False)
                    if result1 >= 0:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                        cvzone.putTextRect(frame, f'{track_id}', (x1, y1), 1, 1)
                        cv2.circle(frame, (x1, y2), 4, (255, 0, 0), -1)

                        if list.count(track_id) == 0:
                            list.append(track_id)

                #### VERIFICAÇÃO DE SAÍDA ####
                result2 = cv2.pointPolygonTest(np.array(area1, np.int32), ((x1, y2)), False)
                if result2 >= 0:
                    exit[track_id] = (x1, y2)

                if track_id in exit:
                    result3 = cv2.pointPolygonTest(np.array(area2, np.int32), ((x1, y2)), False)
                    if result3 >= 0:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                        cvzone.putTextRect(frame, f'{track_id}', (x1, y1), 1, 1)
                        cv2.circle(frame, (x1, y2), 4, (255, 0, 0), -1)

                        if list1.count(track_id) == 0:
                            list1.append(track_id)

    # --------------------------------------------------
    # Exibe contagem total na tela
    # --------------------------------------------------
    enterinshop = len(list)
    exitfromshop = len(list1)
    cvzone.putTextRect(frame, f'{enterinshop}', (50, 60), 1, 1)
    cvzone.putTextRect(frame, f'{exitfromshop}', (50, 100), 1, 1)

    # Desenha as áreas de entrada e saída
    cv2.polylines(frame, [np.array(area1, np.int32)], True, (255, 0, 255), 2)
    cv2.polylines(frame, [np.array(area2, np.int32)], True, (255, 0, 255), 2)

    # Exibe o resultado
    cv2.imshow("RGB", frame)

    # Sai do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Libera os recursos após finalização
cap.release()
cv2.destroyAllWindows()
