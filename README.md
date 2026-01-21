Azure Image Analysis – Computer Vision with Python

Projeto de Visão Computacional utilizando **Azure AI Vision** para análise automática de imagens.  
A aplicação identifica elementos visuais, gera descrições e detecta objetos e pessoas em imagens reais.

---

 Visão Geral

Este projeto demonstra o uso prático de Inteligência Artificial aplicada à análise de imagens, utilizando:

- Serviços de IA na nuvem (Azure AI Vision)
- Integração com Python
- Processamento e anotação visual de imagens
- Detecção automática de pessoas e objetos

O sistema foi desenvolvido como parte do meu portfólio técnico em **IA, Cloud e Engenharia de Software**.

---
Funcionalidades

- Geração automática de legendas para imagens  
- Identificação de elementos visuais (tags)  
- Detecção de objetos  
- Detecção de pessoas  
- Criação de imagens com marcações visuais (bounding boxes)  

---

Tecnologias Utilizadas

- Python 3.11  
- Azure AI Vision (Computer Vision API)  
- Pillow (processamento de imagens)  
- Git & GitHub  

---

Estrutura do Projeto

azure-image-analysis/  
├── image-analysis.py  
├── requirements.txt  
├── README.md  
├── images/  
│   ├── building.jpg  
│   └── person.jpg  

---

Execução do Projeto

Execute o script passando o caminho da imagem:

python image-analysis.py images/building.jpg  
python image-analysis.py images/person.jpg  

---

Resultados

O sistema retorna no terminal:

- Descrição da imagem  
- Elementos identificados  
- Objetos detectados  
- Pessoas detectadas  

Além disso, gera imagens com marcações visuais:

- objects.jpg  
- people.jpg  

Esses arquivos mostram graficamente os objetos e pessoas detectados pela IA.

---

Objetivo do Projeto

Demonstrar habilidades práticas em:

- Integração com serviços de IA em nuvem  
- Desenvolvimento em Python  
- Visão Computacional  
- Uso de APIs de Inteligência Artificial  
- Estruturação de projetos para portfólio  

---

Autor

Thiago Duarte  
Estudante de Engenharia de Software  
Foco em Python, IA e Cloud Computing  

GitHub: https://github.com/tthiagoduarte  

---

Licença

Projeto desenvolvido para fins educacionais e demonstração de competências técnicas.
