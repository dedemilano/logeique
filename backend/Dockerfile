# Utilisation d'une image Python officielle
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de requirements
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . .

ENV PGHOST='ep-divine-poetry-a5pb40al.us-east-2.aws.neon.tech'
ENV PGDATABASE='logeiqueDatabase'
ENV PGUSER='logeiqueDatabase_owner'
ENV PGPASSWORD='sAK67WLdNjBv'

# Commande pour lancer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]