# Azure AI Vision - Image Analysis

Este projeto utiliza o **Azure AI Vision** para analisar imagens e detectar:

- Legendas automáticas (Captions)
- Tags descritivas
- Objetos na imagem
- Pessoas com caixas delimitadoras

## 🛠 Tecnologias usadas

- Python 3
- Azure AI Vision
- Azure SDK
- Pillow (PIL)
- python-dotenv

## 📸 Exemplos

### Detecção de objetos
![Building](examples/building_objects.jpg)

### Detecção de pessoas
![Person](examples/person_people.jpg)

## ⚙️ Configuração

1. Crie um recurso **Azure AI Vision**
2. Copie o **Endpoint** e a **Key**
3. Crie um arquivo `.env` baseado no `.env.example`

```env
VISION_ENDPOINT=SEU_ENDPOINT
VISION_KEY=SUA_CHAVE
