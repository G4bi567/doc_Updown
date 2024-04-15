# Framework #

Dans le développement du jeu "UpDown", trois technologies principales sont utilisées pour enrichir l'expérience du jeu et gérer les interactions en temps réel : WebSockets, p5.js et Matter.js. Chacune de ces technologies joue un rôle spécifique et apporte des fonctionnalités essentielles à la réalisation du jeu.

### WebSockets

WebSockets est une technologie permettant une communication interactive entre un client et un serveur sur le web. Elle est particulièrement utile dans les applications nécessitant une communication en temps réel sans avoir à recharger la page. Dans le contexte de "UpDown", WebSockets est utilisé pour gérer les interactions multijoueurs via le serveur Node.js.

Cette technologie permet de synchroniser l'état du jeu entre tous les joueurs en continu, ce qui est crucial pour les jeux multijoueurs où les actions d'un joueur doivent être immédiatement visibles par les autres joueurs. Grâce à WebSockets, le serveur peut envoyer et recevoir des messages à un faible coût de latence, garantissant ainsi que le gameplay reste fluide et réactif.

### P5.js

p5.js est une bibliothèque JavaScript qui facilite la création de graphiques et d'interactions visuelles dans le navigateur. Elle est largement utilisée pour les projets artistiques et créatifs sur le web, ainsi que pour l'éducation. Dans "UpDown", p5.js est utilisé pour dessiner le décor du jeu, les personnages, et gérer les interactions utilisateur, comme les mouvements du joueur.

Cette bibliothèque offre une grande simplicité pour la mise en place de la boucle de jeu, où chaque frame peut être gérée par une fonction appelée `draw()`, et elle permet de manipuler facilement les éléments visuels. p5.js est aussi appréciée pour sa facilité d'intégration avec d'autres bibliothèques et ses vastes ressources éducatives, ce qui la rend particulièrement accessible pour les développeurs débutants.

### Matter.js

Matter.js est une bibliothèque de physique pour JavaScript qui permet de simuler des corps rigides en 2D. Elle offre des fonctionnalités robustes pour gérer la collision, la gravité, et d'autres propriétés physiques dans les jeux ou les applications interactives. Dans "UpDown", Matter.js est utilisé pour gérer les interactions physiques du jeu, comme les sauts, les chutes, et les collisions entre le joueur et les plateformes ou obstacles.

Avec Matter.js, les développeurs peuvent créer des mondes interactifs complexes avec une relative facilité, rendant les mouvements et les interactions dans le jeu plus réalistes et engageants. Cela ajoute une dimension de réalisme physique au jeu, améliorant l'expérience globale pour les joueurs.

### Interaction entre p5.js et Matter.js

Dans la pratique, p5.js récupère les données de position et d'orientation des objets calculées par Matter.js à chaque frame pour mettre à jour le rendu visuel. Cela signifie que toutes les actions physiques comme sauter, courir, ou tomber sont d'abord calculées par Matter.js en fonction des lois de la physique, et ensuite représentées visuellement par p5.js.

Cette intégration permet de séparer efficacement la logique physique de la représentation visuelle, rendant le développement de jeux plus intuitif et gérable. Matter.js traite les données en arrière-plan, et p5.js s'assure que les joueurs voient ces interactions se dérouler de manière fluide et naturelle à l'écran.