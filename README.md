# \# DevOps Welcome App

# 

# Petite application web Flask qui affiche un message d'accueil configurable.

# 

# \## Image Docker Hub

# 

# `didenala/devops-welcome-app` : versions `1.0.0` et `1.0.1` (alias `1.0`).

# 

# \## Lancer l'application (à partir de l'image seulement)

# 

# ```

# docker run -d --name devops-welcome-app -p 8080:5000 -e GREETING="Votre message" --memory 256m --cpus 0.5 didenala/devops-welcome-app:1.0.1

# ```

# 

# Puis ouvrir http://localhost:8080 dans un navigateur.

# 

# \## Variables d'environnement

# 

# | Variable | Rôle | Valeur par défaut |

# |---|---|---|

# | `GREETING` | Message affiché sur la page d'accueil | `Bonjour depuis Docker !` |

# 

# \## Voir les journaux et arrêter

# 

# ```

# docker logs devops-welcome-app

# docker rm -f devops-welcome-app

# ```

# 

# \## Construire l'image soi-même

# 

# ```

# git clone https://github.com/alaadidene/devops-welcome-app.git

# cd devops-welcome-app

# docker build -t didenala/devops-welcome-app:1.0.1 .

# ```

