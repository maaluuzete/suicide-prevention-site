# Prevenção ao Suícidio 🌻 - IFMS Campus Campo Grande
Este site foi desenvolvido como parte de um trabalho avaliativo de inglês. O objetivo é **promover a conscientização sobre saúde mental e prevenção ao suicídio**, oferecendo informações, apoio e incentivo à empatia emocional. Ainda está em desenvolvimento, o site no Vercel está estático(Plano gratuito tem suas limitações), portanto, as mensagens enviadas não vão para o arquivo `messages.txt`. Só iram se você rodar o projeto localmente em seu próprio computador.

## Sobre o projeto
Este é um projeto educacional e social que busca informar, acolher e inspirar a reflexão sobre o cuidado com a saúde mental. Ele foi desenvolvido com foco em um **design leve, acessível e responsivo**, permitindo uma navegação fluida tanto em computadores quanto em dispositivos móveis.

As seções do site incluem:
- **Home:** introdução ao propósito do projeto.  
- **Talk:** espaço de expressão e compartilhamento de mensagens, onde você pode pedir ajuda ou desabafar. 
- **Healthy Mind:** dicas de bem-estar e autocuidado.  
- **Emotional Empathy:** textos e reflexões sobre empatia.  
- **Team:** apresentação da equipe desenvolvedora do projeto.
---

## Tecnologias utilizadas
- **Frontend:** HTML, CSS e JavaScript. 
- **Backend:** Python com o framework Flask. 
- **Hospedagem:** Render (deploy automático via GitHub).  
---

## Como executar o projeto localmente
### Pré-requisitos
Certifique-se de ter instalado:
- [Python 3.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

### Passos para rodar o projeto
```
# Clone o repositório
git clone https://github.com/maaluuzete/suicide-prevention-site.git
# Acesse a pasta do projeto
cd suicide-prevention-site
cd backend
# Instale as dependências
pip install -r requirements.txt
# Execute o servidor
python app.py
```
Ou acesse o [site](https://suicide-prevention-site.onrender.com/)

## Estrutura do Projeto
```
suicide-prevention-site/
│── README.md
│── LICENSE
│── render.yaml
│── backend/
│   └── app.py
|   └── messages.txt
│   └── requirements.txt
│── frontend/
│   ├── templates/
│   │   ├── index.html
│   │   ├── healthy.html
│   │   ├── emotional_empathy.html
│   │   ├── talk.html
│   │   └── team.html
│   ├── css/
│   │   └── style.css
|   ├── js/
│   │   └── app.js
│── assets/
│   └── (...)
```
* `render.yaml` → Configurações do deploy na Render.
* `requirements.txt` → Dependências Python (Flask, etc).
* `backend/` → Contém o código servidor (app.py).
* `frontend/` → Parte visual do site (HTML, CSS e JavaScript).
* `assets/` → Contém as imagens utilizadas.
* `messages.txt` → arquivo onde são salvas as mensagens enviadas pelo formulário.
## Licença
Este projeto está licenciado sob a licença MIT. Para mais detalhes, consulte [LICENSE](https://github.com/maaluuzete/suicide-prevention-site?tab=MIT-1-ov-file) incluído neste repositório.
