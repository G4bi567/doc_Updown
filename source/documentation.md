# Documentation #



### Fichier : `index.html`
**Description Générale :**
Ce fichier HTML constitue le squelette du jeu "UpDown". Il sert de point d'entrée pour l'utilisateur, intégrant tous les éléments visuels, les interactions, et les scripts nécessaires pour le fonctionnement du jeu. Le fichier organise les interfaces utilisateur pour différentes interactions comme la sélection du mode de jeu, la gestion du lobby multijoueur, les options de son, et les notifications en jeu.

**Contenu et Fonctionnalités :**

#### 1. En-tête (`<head>`)
- **Fonctionnalités :**
  - Définit l'encodage des caractères.
  - Lie le fichier CSS pour le style.
  - Établit le titre de la page web affiché dans l'onglet du navigateur.

#### 2. Corps (`<body>`)
- **Menu Principal (`<div id="menu">`):**
  - **Boutons de Mode de Jeu :** Trois boutons permettant de démarrer le jeu en mode solo, local ou multijoueur. Chaque bouton déclenche la fonction `startGame()` avec un argument correspondant au mode de jeu choisi.
    - **`startGame(mode)`** :
      - **Paramètres :** `mode` (string) - Le mode de jeu à initialiser.
      - **Action :** Initialise le jeu dans le mode spécifié, préparant les configurations et l'interface nécessaire.

- **Lobby Multijoueur (`<div id="multiplayerLobby">`):**
  - Permet aux joueurs de saisir un surnom et un ID de lobby pour créer ou rejoindre une session multijoueur.
  - **`joinLobby()`** et **`createNewLobby()`** :
    - **Action :** Ces fonctions contrôlent l'interaction avec le serveur pour gérer les sessions multijoueurs, permettant aux joueurs de se connecter entre eux via WebSockets.

- **Options Audio (`<div id="optionsMenu">`):**
  - Propose des contrôles pour ajuster le volume de différents effets sonores et de la musique de fond.
  - **`saveOptions()`** :
    - **Action :** Sauvegarde les réglages modifiés par l'utilisateur, appliquant les préférences de volume pour améliorer l'expérience de jeu personnalisée.

- **Notifications et Messages (`<div class="ninja-popup">`):**
  - Fournit des informations contextuelles et des encouragements grâce à des popups qui apparaissent en réponse à des événements spécifiques du jeu.
  - **`closePopup()`** :
    - **Action :** Ferme le popup actuellement affiché, permettant à l'utilisateur de continuer son jeu sans interruption.

- **Scripts :**
  - Charge les bibliothèques et scripts essentiels , comme `sketch.js`et `multiplayer.js`, pour la mécanique du jeu, la gestion des événements et la communication réseau, tels que `socket.io`, `p5.js`, et `matter.js`.

### Fichier : `sketch.js`
**Description Générale :**
Ce script centralise la logique de contrôle, l'initialisation du jeu, la gestion des interactions des joueurs, la physique du jeu, et le contrôle multimédia pour "UpDown". Le fichier orchestre les différentes phases du jeu et gère les entrées des utilisateurs.

#### Initialisation et Configuration
**`startGame(mode_name)`**
  - **But :** Initialise le jeu en fonction du mode sélectionné.
  - **Détail :** Configure les paramètres de jeu et prépare l'environnement en fonction du mode (solo, local, multiplayer).

**`initializeGame()`**
  - **But :** Configure les éléments essentiels du jeu.
  - **Détail :** Prépare le moteur de jeu et initialise le canvas.

**`setup()`**
  - **But :** Met en place le canvas et les objets du jeu.
  - **Détail :** Crée les joueurs et configure le moteur physique.

#### Gestion des Joueurs
**`createPlayer(x, y, label)`**
  - **But :** Crée un joueur à une position spécifiée.
  - **Détail :** Initialise un joueur avec des coordonnées et une étiquette.

#### Gestion de l'Audio
**`toggleBackgroundMusic()`**
  - **But :** Bascule la musique de fond on/off.
  - **Détail :** Contrôle la lecture de la musique en fonction de l'état actuel.

**`preload()`**
  - **But :** Charge les ressources nécessaires.
  - **Détail :** Précharge les images et les sons utilisés dans le jeu.

**`setupSounds()`**
  - **But :** Configure les paramètres sonores initiaux.
  - **Détail :** Définit les niveaux de volume pour différents effets sonores et musique.

#### Contrôle des Interactions
**`playWalkSound()`**
  - **But :** Joue un son de marche sous certaines conditions.
  - **Détail :** Vérifie le timing pour jouer un son de pas.

**`handleKeyDown(event)`** et **`handleKeyUp(event)`**
  - **But :** Réagit aux événements clavier.
  - **Détail :** Met à jour l'état des touches et applique les commandes de jeu.

**`handleGameControls(event)`**
  - **But :** Gère les actions basées sur les touches appuyées.
  - **Détail :** Déclenche des actions comme sauter ou attaquer en fonction de la touche.

#### Logique du Jeu
**`updateGame()`**
  - **But :** Met à jour l'état du jeu en mode multijoueur.
  - **Détail :** Envoie l'état du joueur via WebSocket.

**`checkGameConditions()`**
  - **But :** Vérifie les conditions de victoire ou d'avancement.
  - **Détail :** Applique les règles du jeu pour vérifier si les joueurs ont atteint les objectifs.

**`draw()`**
  - **But :** Fonction principale de rendu appelée à chaque frame.
  - **Détail :** Gère l'affichage du jeu, dessine les éléments du jeu et vérifie les conditions.

#### Gestion des Événements et des États
**`showPopup()`, `closePopup()`, `showVictoryPopup()`**
  - **But :** Affiche et gère les popups pour divers événements.
  - **Détail :** Contrôle l'affichage des notifications et des messages de victoire.

**`resetGame()`**
  - **But :** Réinitialise le jeu à ses états par défaut.
  - **Détail :** Prépare le jeu pour une nouvelle session après la fin d'une partie.

#### Fonctions Auxiliaires
**`applyWindForce(player)`**, **`checkPlayerInteractions(player)`**, etc.
  - **But :** Applique des forces et vérifie les interactions.
  - **Détail :** Gère les interactions spécifiques comme le vent et les collisions.

### Fichier : `multiplayer.js`
Voici une description détaillée des fonctions du fichier multiplayer.js. Ce fichier gère principalement l'interface utilisateur pour les interactions multijoueur, la communication avec le serveur via WebSockets, et la gestion de la création de lobby et du processus d'adhésion des joueurs.
#### Gestion du lobby et des interactions multijoueur
#### **`toggleMultiplayerLobby()`**
  - **Objectif :** Bascule la visibilité de l'interface du lobby multijoueur.
  - **Détails :** Alterne la propriété de display de l'élément du lobby entre 'block' et 'none', le montrant ou le cachant en conséquence.

#### **`showMultiplayerOptions()`**
  - **Objectif :** Affiche les options multijoueur et masque les autres éléments liés au multijoueur.
  - **Détails :** Rend visible la section des options multijoueur et cache les sections du lobby et de création de nouveau lobby.

#### **`showJoinLobby()`**
  - **Objectif :** Prépare l'interface utilisateur pour rejoindre un lobby existant.
  - **Détails :** Affiche l'interface utilisateur du lobby multijoueur pour l'entrée de l'ID de lobby et masque les autres sections.

#### **`createNewLobby()`**
  - **Objectif :** Initie le processus de création d'un nouveau lobby.
  - **Détails :** 
    - Se connecte au serveur WebSocket.
    - À la connexion réussie, émet un événement 'createLobby' avec un ID de lobby unique et le pseudonyme du joueur.
    - Écoute l'événement 'lobbyCreated' pour confirmer la création du lobby, puis masque l'interface du lobby et affiche l'ID du lobby.
    - Gère les erreurs de connexion et les délais d'attente.

#### **`joinLobby()`**
  - **Objectif :** Gère le processus de rejoindre un lobby existant.
  - **Détails :** 
    - Se connecte au serveur WebSocket.
    - À la connexion réussie, émet un événement 'joinLobby' avec l'ID de lobby spécifié et le pseudonyme.
    - Écoute l'événement 'joinedLobby' pour confirmer l'adhésion, puis met à jour l'interface utilisateur pour montrer l'ID du lobby et masque le formulaire d'entrée.
    - Gère les erreurs de connexion et les délais d'attente.

#### **`copyLobbyId()`**
  - **Objectif :** Copie l'ID du lobby actuel dans le presse-papiers.
  - **Détails :** Utilise l'API Clipboard pour copier l'ID du lobby et fournit un retour à l'utilisateur en cas de succès ou d'échec.
### Fichier : `player.js`

La classe Player dans player.js est conçue pour encapsuler les propriétés et les comportements d'un personnage de joueur dans le jeu. 
#### Classe : `Player`
**Description générale :**
Cette classe représente un joueur dans le jeu, gérant ses propriétés physiques, son animation, et ses interactions en jeu.

#### **`constructor(x, y, w, h)`**
  - **Objectif :** Initialise un nouveau joueur avec des dimensions et une position spécifiques.
  - **Détails :**
    - **`x`, `y` :** Coordonnées initiales du joueur.
    - **`w`, `h` :** Largeur et hauteur du joueur.
    - Initialise les propriétés du joueur, charge les sprites, et définit les paramètres d'animation et de physique.

#### **`setPosition(x, y)`**
  - **Objectif :** Définit la position du joueur.
  - **Paramètres :**
    - **`x`, `y` :** Nouvelles coordonnées du joueur.

#### **`setSize(w, h)`**
  - **Objectif :** Définit les dimensions du joueur et ajuste le zoom.
  - **Paramètres :**
    - **`w`, `h` :** Largeur et hauteur du joueur.

#### **`setPhysicsOptions()`**
  - **Objectif :** Configure les options de physique pour le corps du joueur.
  - **Détails :** Définit la friction, l'inertie, la restitution, et d'autres propriétés physiques.

#### **`loadSprites()`**
  - **Objectif :** Charge les images pour différentes animations du joueur.
  - **Détails :** Charge des sprites pour l'idle, la course, le saut, la chute, le coup reçu, et l'attaque.

#### **`initializeAnimationProperties()`**
  - **Objectif :** Initialise les propriétés nécessaires pour l'animation.
  - **Détails :** Définit la largeur, la hauteur, et le nombre de frames pour les animations, ainsi que la fréquence des frames.

#### **`setGaugeSettings()`**
  - **Objectif :** Configure les paramètres pour la jauge d'attaque.
  - **Détails :** Définit la largeur, la hauteur, et la visibilité de la jauge d'attaque.

#### **`show()`**
  - **Objectif :** Affiche le joueur à chaque frame du jeu.
  - **Détails :** Sélectionne et affiche le sprite approprié basé sur l'état actuel du joueur et met à jour l'animation.

#### **`displaySprite(sprite, scaledWidth, scaledHeight)`**
  - **Objectif :** Affiche un sprite spécifique avec les dimensions données.
  - **Détails :** Calcule l'indice de frame à utiliser et applique l'image sur le canvas.

#### **`shouldFlipSprite()`**
  - **Objectif :** Détermine si le sprite doit être retourné.
  - **Détails :** Retourne le sprite en fonction de l'orientation du joueur.

#### **`resetAnimation()`**
  - **Objectif :** Réinitialise l'animation au début.
  - **Détails :** Remet le compteur de frames à zéro.

#### **`attackResetAnimation()`**
  - **Objectif :** Réinitialise spécifiquement l'animation d'attaque.
  - **Détails :** Positionne l'animation d'attaque à un certain point pour synchroniser avec l'action.

#### **`updateAnimationFrame()`**
  - **Objectif :** Met à jour l'indice de frame pour l'animation.
  - **Détails :** Incrémente le compteur de frames et ajuste l'indice de frame actuel selon la fréquence définie.

#### **`determineAnimationState()`**
  - **Objectif :** Détermine l'état d'animation actuel basé sur les conditions du jeu.
  - **Détails :** Vérifie les conditions comme être touché, attaquer, sauter, tomber, ou courir pour déterminer l'état.

#### **`isHit()`, `isJumping()`, `isFalling()`, `isRunning()`, `isAttacking()`**
  - **Objectif :** Séries de fonctions pour vérifier l'état du joueur.
  - **Détails :** Chaque fonction

 vérifie une condition spécifique basée sur la physique ou les actions du joueur.

#### **`applyForce(force)`**
  - **Objectif :** Applique une force externe au corps du joueur.
  - **Paramètres :**
    - **`force` :** Vecteur de force à appliquer.


### Fichier : `boundary.js`

La classe `Boundary` dans `boundary.js` est conçue pour représenter des limites physiques dans le jeu, comme des murs ou des plates-formes, qui ne bougent pas et influencent la physique des autres objets en jeu.

#### Classe : `Boundary`
**Description générale :**
Cette classe sert à créer et à gérer des objets statiques dans le monde du jeu, utilisés principalement pour les collisions et les barrières environnementales.

#### **`constructor(x, y, w, h)`**
  - **Objectif :** Initialise une nouvelle frontière ou limite avec des dimensions et une position spécifiques.
  - **Paramètres :**
    - **`x`, `y` :** Coordonnées de la position initiale de la frontière.
    - **`w`, `h` :** Largeur et hauteur de la frontière.
  - **Détails :**
    - **`options` :** Configuration des options physiques, indiquant que l'objet est statique et sans restitution pour éviter le rebondissement.
    - Crée un rectangle physique qui sera utilisé comme frontière dans le moteur de physique.

#### **`show()`**
  - **Objectif :** Affiche la frontière dans le canvas.
  - **Détails :**
    - Récupère la position et l'angle actuels de l'objet dans le moteur physique.
    - Utilise la fonction `translate()` pour positionner le rectangle au bon endroit dans le canvas.
    - Applique une rotation si nécessaire.
    - Dessine un rectangle pour représenter visuellement la frontière.
    - Utilise `rectMode(CENTER)` pour s'assurer que le rectangle est centré sur ses coordonnées.
    - Configure le style de dessin avec `noStroke()` et un remplissage transparent pour une intégration visuelle simple.


### Fichier : `config.js`
**Description générale :**
Ce script contient la configuration globale pour les aspects du jeu qui peuvent nécessiter un ajustement ou une référence centralisée, tels que les volumes sonores des différentes actions ou de la musique de fond.

#### **Configuration : `GameConfig`**
  - **Objectif :** Fournir un accès centralisé aux paramètres de configuration du jeu.
  - **Structure :**
    - **`soundVolumes` :** Un objet qui contient les configurations de volume pour différents effets sonores et la musique de fond.
      - **`movement` :** Volume pour les sons de mouvement, réglé à 0.2. Cela peut inclure les bruits de pas ou d'autres sons liés au déplacement du personnage.
      - **`landing` :** Volume pour les sons d'atterrissage, réglé à 0.2. Utilisé pour les bruits produits lorsque le personnage atterrit après un saut ou une chute.
      - **`jump` :** Volume pour les sons de saut, réglé à 0.3. Couvre les effets sonores déclenchés lorsqu'un personnage saute.
      - **`backgroundMusic` :** Volume pour la musique de fond, réglé à 0.08. Ce paramètre affecte le volume global de la musique qui joue en arrière-plan pendant le jeu.

#### Utilisation :
Cette configuration peut être importée et utilisée dans d'autres scripts pour appliquer les réglages de volume aux éléments appropriés, assurant une expérience auditive cohérente et personnalisable à travers le jeu. Par exemple, lors de l'initialisation des sons dans le jeu, on peut accéder à ces valeurs pour régler les volumes de chaque son de manière appropriée.

Pour intégrer les données de collision spécifiées dans le tableau `floorCollision` dans le contexte du développement du jeu, on peut les utiliser pour définir où les blocs de collision statiques devraient être positionnés dans l'environnement de jeu. Voici une explication de la manière dont ces données pourraient être utilisées dans le contexte d'un fichier comme `Ground.js`:

### Fichier : `Ground.js`
**Description générale :**
Ce fichier est destiné à gérer et à initialiser les blocs de collision au sol par rapport à l'image de fond dans le jeu en utilisant la bibliothèque de physique Matter.js. Ces blocs définissent les zones où les personnages peuvent marcher ou interagir physiquement.

#### Définition des blocs de collision
**`floorCollision` : Array**
  - **Objectif :** Stocker les données de collision pour le sol.
  - **Structure :** Un tableau de valeurs qui indique où les blocs de collision doivent être créés. Chaque valeur non-nulle (`3193` dans ce cas) dans le tableau représente un bloc solide de 16x16 pixels où les personnages ne peuvent pas passer.

#### Utilisation :
La structure `floorCollision` peut être interprétée pour générer des instances de la classe `Boundary` pour chaque bloc de collision actif. Voici un exemple de fonction qui pourrait être utilisée pour créer ces blocs à partir des données de collision :

```javascript
// Fonction pour créer des blocs de collision à partir des données floorCollision
function createFloorBlocks(data) {
    const tileSize = 16; // La taille de chaque bloc en pixels
    const tileOffset = 50; // Un décalage de base pour la position y

    data.forEach((value, index) => {
        if (value !== 0) { // Si la valeur est non-nulle, créer un bloc
            const x = (index % 100) * tileSize; // Calcul de la position x
            const y = Math.floor(index / 100) * tileSize + tileOffset; // Calcul de la position y

            // Création de l'objet Boundary et ajout au monde de jeu
            const block = new Boundary(x, y, tileSize, tileSize);
            Composite.add(world, block.body);
        }
    });
}

// Exemple d'appel de la fonction
createFloorBlocks(floorCollision);
```

Ce code prend en compte chaque élément du tableau `floorCollision`. Si la valeur de l'élément est non-nulle, il crée un bloc à la position correspondante. Chaque bloc est positionné en calculant sa position `x` et `y` basée sur son index dans le tableau et la taille des blocs définie (ici 16 pixels par bloc). Les blocs sont ensuite ajoutés au monde physique pour interagir avec d'autres objets physiques comme les personnages.

Cela permet une gestion flexible et dynamique des environnements de jeu où les éléments de collision sont définis par des structures de données simples, facilitant les ajustements et l'expansion du monde du jeu.

### Fichier : `platform.js`
**Description générale :**
Ce fichier sert à initialiser les plateformes de collision dans le jeu à partir d'un tableau prédéfini, utilisant la bibliothèque de physique Matter.js. Les plateformes définies ici sont essentielles pour les interactions physiques telles que marcher, sauter, ou toute autre interaction nécessitant une surface solide.

#### Définition des plateformes de collision
**`platformCollision` : Array**
  - **Objectif :** Stocker les données de collision pour les plateformes.
  - **Structure :** Un tableau de valeurs qui indique où les plateformes doivent être créées dans le niveau. Les valeurs spécifiques (par exemple, `1400`) indiquent un type particulier de bloc.

#### Utilisation :
Les données dans `platformCollision` sont utilisées pour générer des instances de la classe `Boundary` pour chaque plateforme nécessaire.

Dans ce code, chaque élément non nul du tableau `platformCollision` entraîne la création d'une plateforme. Les plateformes sont ensuite ajoutées au monde physique, où elles peuvent interagir avec d'autres éléments physiques du jeu.

### Fichier : `style.css`
**Description générale :**
Ce fichier CSS est conçu pour styliser l'interface utilisateur et les éléments interactifs du jeu, en utilisant une palette de couleurs basée sur des teintes de vert et des arrière-plans sombres pour créer une ambiance visuelle cohérente et engageante.

#### Structure principale
**`main` :**
  - **Objectif :** Définir la présentation de base de la zone de jeu ou de l'application.


#### Menus et interactions
**`#menu` :**
  - **Usage :** Positionnement central pour les menus de jeu, utilisant une transformation pour un alignement parfait au centre. Le style visuel favorise la lisibilité avec du texte blanc sur fond sombre.

**`.button` et `button` :**
  - **Objectif :** Boutons stylisés avec des bordures arrondies et une couleur de fond vert forêt pour une meilleure intégration dans le thème général du jeu.
  - **Interactivité :** Effet de survol qui assombrit la couleur de fond pour indiquer la possibilité d'interaction.

#### Popups et composants interactifs
**`.ninja-popup` :**
  - **Fonction :** Utilisé pour des notifications ou des dialogues modaux, avec un fond sombre semi-transparent qui permet de concentrer l'attention sur le contenu.
  - **Esthétique :** Texte blanc et ombre portée verte pour un impact visuel fort, renforçant l'aspect ludique du jeu.

#### Entrées et formulaires
**`input[type="text"]` :**
  - **Design :** Entrées textuelles avec bordure grise et arrondie pour une intégration esthétique douce et une expérience utilisateur cohérente.
  
#### Gestion avancée des options
**`#optionsMenu` :**
  - **Rôle :** Conteneur pour les réglages et options du jeu, avec une position fixe au centre et un arrière-plan sombre pour une immersion sans distraction.
  - **Eléments interactifs :** Sliders avec poignées blanches sur fond vert, soulignant l'aspect interactif et dynamique du menu.

### Fichier : `sprite`

**Description générale :**
Le dossier `sprite` est une ressource essentielle dans le développement de jeux, car il contient des éléments visuels et sonores qui contribuent directement à l'ambiance et à l'interface utilisateur du jeu. Il est structuré pour inclure plusieurs sous-dossiers, chacun dédié à un type de contenu spécifique.

#### Contenu du dossier `sprite`
1. **Sprites du personnage :**
   - **Usage :** Ce sous-dossier contient les images animées du personnage principal. Ces sprites sont utilisés pour représenter diverses actions et états du personnage, comme la course, le saut, et d'autres animations.

2. **Logo du jeu :**
   - **Fonction :** Ce fichier est généralement utilisé pour le menu principal à travers le jeu.

3. **Sons :**
   - **Contenu :** Ce sous-dossier inclut les fichiers audio utilisés pour les effets sonores du jeu, comme les bruitages de pas, les sons d'actions (sauts, attaques), ainsi que les ambiances et musiques de fond.

4. **Image de fond (Background Image) :**
   - **Utilisation :** Les images de fond sont employées pour créer les environnements dans lesquels les niveaux du jeu se déroulent. 
