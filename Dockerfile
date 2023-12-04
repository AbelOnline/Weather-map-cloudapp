# Utilisez une image Python de base
FROM python:3.8

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/requirements.txt

# Définissez le répertoire de travail
WORKDIR /app

# Installez les dépendances à partir du fichier requirements.txt
RUN pip install -r requirements.txt

# Copiez le reste de votre application dans le conteneur
COPY . /app

# Commande pour exécuter votre application (ajustez selon vos besoins)
CMD ["python", "main.py"]
