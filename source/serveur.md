# Serveur #

Le fichier `server.js` constitue le cœur du serveur pour le jeu "UpDown", et il est essentiel pour orchestrer les interactions multijoueur via WebSockets. Implémenté en Node.js et utilisant les bibliothèques `http` et `socket.io`, ce script gère la communication en temps réel nécessaire au bon fonctionnement du jeu en mode multijoueur. Voici une exploration détaillée de ses composantes et fonctionnalités principales.

### Configuration et mise en place du serveur

Dès le début du script, un serveur HTTP basique est mis en place avec Node.js en utilisant le module `http`. Ce serveur est configuré spécifiquement pour gérer les requêtes CORS, en ajustant les en-têtes appropriés pour permettre aux interactions de se faire sans accroc entre le client, potentiellement hébergé sur une origine différente, et ce serveur.

### Utilisation de Socket.IO

L'intégration de `socket.io` est cruciale car elle permet une communication fluide et en temps réel entre les clients (les joueurs) et le serveur. Cette bibliothèque est idéale pour les applications nécessitant des interactions instantanées, comme c'est le cas dans les jeux en ligne multijoueurs où la synchronisation de l'état du jeu entre les joueurs doit être impeccable.

### Gestion des lobbies

Le serveur joue un rôle clé dans la création et la gestion des lobbies, qui sont essentiels pour organiser les sessions de jeu multijoueur :
- **`createLobby`** : Les joueurs peuvent initier la création de lobbies avec un ID unique. Si le lobby est créé avec succès, le serveur envoie les détails du lobby au joueur initiateur.
- **`joinLobby`** : Les joueurs peuvent rejoindre des lobbies existants, en assumant le rôle de joueur.

### Événements et interactions gérées

- **Connexions et déconnexions** : Chaque connexion (`connection`) ou déconnexion (`disconnect`) d'un joueur est soigneusement traitée pour assurer la mise à jour et l'intégrité de l'état du lobby.
- **Mise à jour de l'état du joueur** (`updatePlayerState`): Les actions des joueurs, telles que les mouvements ou les attaques, sont partagées en temps réel avec tous les joueurs du même lobby pour garantir une expérience de jeu cohérente.
- **Gestion des attaques** (`playerAttack`): Les interactions spécifiques comme les attaques sont également gérées par le serveur, reflétant ces actions à tous les participants du lobby.

### Gestion des erreurs

Le serveur est également équipé pour gérer les erreurs, envoyant des messages d'erreur aux clients en cas d'échec de création ou de connexion à un lobby, offrant ainsi une expérience utilisateur robuste et réactive.

### Démarrage du serveur

Enfin, le serveur est configuré pour écouter sur un port défini par la variable d'environnement `PORT` ou, à défaut, sur le port 3000.