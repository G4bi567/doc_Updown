# Installation #
### Configuration de l'Environnement pour le Mode Local

1. **Installation de Node.js** : Vérifiez que Node.js est installé sur votre machine. Si ce n'est pas le cas, vous pouvez le télécharger et l'installer depuis le site [nodejs.org](https://nodejs.org/).

2. **Ouvrir votre Interface de Commande (CLI)** : Ouvrez votre terminal et naviguez jusqu'au dossier contenant les fichiers du jeu.

3. **Démarrage d'un Serveur Local** :
   - Installez un package de serveur HTTP en exécutant la commande `npm install http-server -g`.
   - Lancez le serveur en exécutant `http-server` dans le dossier du jeu.

4. **Accès au Jeu** :
   - Ouvrez votre navigateur et saisissez l'URL `http://localhost:8080`.
   - Accédez au fichier `index.html` pour démarrer le jeu.

5. **Jouer** :
   - Pour le joueur 1, utilisez les touches `W, A, S, D, G`.
   - Pour le joueur 2, utilisez les touches directionnelles et `L`.

### Configuration et Lancement du Serveur Multijoueur

1. **Prérequis** : Assurez-vous que Node.js est installé sur votre machine.

2. **Installation des Dépendances** :
   - Ouvrez votre CLI et naviguez jusqu'au dossier `server` dans les fichiers du jeu.
   - Exécutez `npm install` pour installer les dépendances nécessaires.

3. **Démarrage du Serveur** :
   - Exécutez `node server.js` pour lancer le serveur sur le port par défaut 3000.

4. **Connexion au Serveur depuis le Jeu** :
   - Configurez le jeu pour se connecter à l'adresse `http://localhost:3000` pour les interactions multijoueur.
   - Si le serveur est sur une autre machine ou un port différent, ajustez les configurations dans le jeu en conséquence.

5. **Tester le Serveur** :
   - Ouvrez deux fenêtres de navigateur pour tester le mode multijoueur.
   - Connectez chaque instance du jeu au serveur pour vérifier le bon fonctionnement des interactions entre joueurs.
