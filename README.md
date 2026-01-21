# Azure Image Analysis 

Projeto de análise de imagens utilizando **Azure AI Vision** com **Python**.  
O sistema gera legendas automáticas, identifica tags, detecta objetos e localiza pessoas em imagens.

---

##  Funcionalidades

- Geração de legendas (captions)
- Geração de legendas detalhadas (dense captions)
- Identificação de tags relevantes
- Detecção de objetos
- Detecção de pessoas com bounding boxes
- Geração de imagens anotadas (`objects.jpg` e `people.jpg`)

---

##  Tecnologias

- Python 3.11  
- Azure AI Vision (Computer Vision API)  
- Pillow  
- python-dotenv  
- Git & GitHub  

---

##  Estrutura do projeto

azure-image-analysis/  
├── image-analysis.py  
├── requirements.txt  
├── .env.example  
├── README.md  
├── images/  
│   ├── building.jpg  
│   └── person.jpg  

---

##  Configuração

### 1 Clonar o repositório

git clone https://github.com/tthiagoduarte/azure-image-analysis.git  
cd azure-image-analysis  

### 2 Criar o arquivo .env

Crie um arquivo chamado `.env` com:

VISION_ENDPOINT=https://SEU-ENDPOINT.cognitiveservices.azure.com/  
VISION_KEY=SUA_CHAVE_DO_AZURE  

⚠️ Nunca publique sua chave no GitHub.

### 4 Instalar dependências

pip install -r requirements.txt  

---

##  Executar

python image-analysis.py images/building.jpg  
python image-analysis.py images/person.jpg  

---

##  O que o programa faz

Mostra no terminal:

- Caption da imagem  
- Dense captions  
- Tags  
- Objetos detectados  
- Pessoas detectadas  

E gera:

- objects.jpg  
- people.jpg  

---

##  Segurança

O arquivo `.env` está no `.gitignore` para proteger suas credenciais.

---

##  Autor

Thiago Duarte  
Estudante de Engenharia de Software  
Python | IA | Azure  
GitHub: https://github.com/tthiagoduarte  


