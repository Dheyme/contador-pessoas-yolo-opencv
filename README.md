# 📊 Contador de Pessoas com YOLOv8 + OpenCV

Este é um projeto em Python que utiliza **YOLOv8** e **OpenCV** para **detectar, rastrear e contar pessoas** entrando e saindo de uma área específica em um vídeo. Ideal para aplicações como monitoramento de lojas, eventos, segurança, entre outros.

---

## 🎯 Objetivo

Desenvolver um sistema simples e eficiente para contagem de pessoas usando visão computacional. Este repositório será a base para melhorias futuras como:
- Interface gráfica (GUI)
- Exportação de dados
- Dashboard web
- Banco de dados

---

## 🛠 Tecnologias Utilizadas

- [Python 3.8+](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [YOLOv8 (Ultralytics)](https://docs.ultralytics.com/)
- [cvzone](https://github.com/cvzone/cvzone)
- [Thonny IDE](https://thonny.org/)

---

## 💻 Como rodar o projeto no Thonny

### 1. Instale o Thonny

Baixe e instale o Thonny pelo site oficial:  
👉 [https://thonny.org](https://thonny.org)

---

### 2. Abra o projeto no Thonny

1. Baixe ou clone este repositório no seu computador.
2. Abra o **Thonny**.
3. No menu superior, clique em **"Arquivo > Abrir..."** e selecione o arquivo `main.py`.

---

### 3. Instale as bibliotecas necessárias no Thonny

Com o Thonny aberto:

1. Vá até o menu: **"Ferramentas > Gerenciar pacotes"**
2. Pesquise e instale os seguintes pacotes (um por um):

opencv-python numpy ultralytics cvzone

> ⚠️ Pode demorar alguns minutos dependendo da sua internet.

---

### 4. Coloque os arquivos necessários na mesma pasta

Na mesma pasta do `main.py`, coloque:

- ✅ O link do video esta no arquivo de texto: vid.txt, para fazer download do arquivo `peoplecount1.mp4`
- ✅ Verifica se o modelo YOLO chamado `yolo11n.pt` esta já na pasta

> Você pode baixar modelos da [Ultralytics](https://github.com/ultralytics/ultralytics) ou treinar o seu próprio.

---

### 5. Execute o código

Com tudo instalado e configurado:

1. Clique no botão **"Executar"** (ícone ▶️ no topo da janela)
2. O vídeo será exibido em uma janela chamada `RGB`
3. A contagem de entradas e saídas aparecerá em tempo real

Pressione **Q** na janela de vídeo para encerrar.

## 🎥 Demonstração

Veja o sistema de contagem de pessoas em ação:

![Image](https://github.com/user-attachments/assets/b0338d29-bded-47d7-984e-fb3e82c3afe1)

![Image](https://github.com/user-attachments/assets/dea18d85-3027-4064-b338-07e3b84a7541)

![Image](https://github.com/user-attachments/assets/2016efec-9a00-4b6f-b158-5f2dafa88b7c)

---

## 📂 Estrutura do Projeto

contador-pessoas-yolo-opencv/ │ ├── main.py # Código principal (com comentários didáticos) ├── peoplecount1.mp4 # Vídeo de teste (adicione o seu) ├── yolo11n.pt # Modelo YOLOv8 (adicione o seu) └── README.md # Este arquivo


---

## 📈 Roadmap

- [ ] Exportação para CSV
- [ ] Interface gráfica com Tkinter
- [ ] Dashboard com gráficos de contagem
- [ ] Suporte para múltiplos vídeos ou câmeras
- [ ] Integração com banco de dados (SQLite ou Firebase)

---

## 🙋‍♂️ Suporte

Caso tenha dúvidas, sugestões ou queira contribuir, sinta-se à vontade para abrir uma **issue** ou me chamar!

---

## 📄 Licença

Este projeto está sob a licença MIT – use, modifique e compartilhe à vontade.

---



