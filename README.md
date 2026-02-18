# OmBot

Un chatbot intelligent construit avec Streamlit et OpenRouter API.

## Fonctionnalités

- Interface utilisateur moderne et épurée
- Historique des conversations
- Multiple modèles d'IA via OpenRouter
- Design professionnel type SaaS
- Suggestions rapides pour démarrer

## Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/VOTRE_USERNAME/ombot.git
cd ombot
```

2. Créez un environnement virtuel :
```bash
python -m venv .venv
```

3. Activez l'environnement virtuel :
- Windows : `.venv\Scripts\activate`
- Mac/Linux : `source .venv/bin/activate`

4. Installez les dépendances :
```bash
pip install streamlit python-dotenv requests
```

5. Créez un fichier `.env` avec votre clé API OpenRouter :
```
OPENROUTER_API_KEY=votre_clé_api_ici
```

6. Lancez l'application :
```bash
streamlit run app.py
```

## Configuration

Obtenez une clé API gratuite sur [OpenRouter](https://openrouter.ai)

## Technologies

- **Streamlit** - Framework web Python
- **OpenRouter API** - Accès aux modèles d'IA
- **Python-dotenv** - Gestion des variables d'environnement

## Licence

MIT
