(regard-critique)=

### Regard critique 

**Analyse des objectifs par rapport aux technologies utilisées :**
L'adoption de nouvelles technologies telles que Matter.js et p5.js pour ce projet a été un choix ambitieux visant à tirer profit de leurs puissantes fonctionnalités pour la physique et le rendu graphique dans un environnement de jeu. Cependant, l'utilisation de ces bibliothèques a présenté des défis particuliers, notamment dans la gestion des sprites et la mise en œuvre d'une caméra pour le multijoueur local.

**Difficultés rencontrées :**
1. **Utilisation des Sprites :** La manipulation des sprites avec p5.js s'est avérée complexe, surtout en ce qui concerne l'animation des personnages et leur intégration avec la physique de Matter.js. La synchronisation des animations avec les actions physiques a nécessité une compréhension approfondie des deux bibliothèques.
2. **Gestion de la Caméra pour Multijoueur Local :** La création d'une vue de caméra qui suit plusieurs joueurs à la fois sur un seul écran a été techniquement exigeante. Gérer les différents points de vue sans perdre le focus sur les actions des joueurs a été une tâche ardue.
3. **Configuration du Serveur et Réseau :** L'implémentation du serveur avec Node.js et la gestion des sockets pour supporter un gameplay fluide et synchrone entre plusieurs joueurs a posé plusieurs problèmes. Les défis incluaient la latence réseau et la synchronisation des états de jeu entre les clients.

**Solutions proposées :**
- **Formation et Ressources :** Augmenter la formation sur les bibliothèques spécifiques utilisées, telles que Matter.js et p5.js, et lire des forums en ligne peut aider à surmonter les obstacles techniques plus rapidement.
- **Amélioration de la Gestion des Sprites :** Développer des scripts plus robustes pour l'animation des sprites qui gèrent mieux les interactions avec la physique du jeu. Utiliser des outils de débogage pour visualiser et ajuster les interactions en temps réel.
- **Optimisation de la Caméra :** Implémenter des algorithmes de caméra plus avancés qui peuvent dynamiquement ajuster la vue en fonction de la position et de l'activité des joueurs, assurant ainsi que tous les joueurs restent visibles.
- **Renforcement des Capacités du Serveur :** Améliorer les mécanismes de gestion des sockets pour réduire la latence et améliorer la synchronisation des données.

### Amélioration

**Améliorations pour les objectifs non atteints :**

Un des objectifs initiaux non atteints était la mise en place d'un serveur toujours actif et non local pour supporter un gameplay multijoueur en ligne sans interruptions. Cette infrastructure est cruciale pour permettre à des joueurs distants de se connecter et interagir en temps réel, ce qui est essentiel pour l'expansion du jeu à une audience plus large.

**Difficultés rencontrées :**
- **Infrastructure Serveur :** La gestion d'un serveur local pour les tests ne pose pas les mêmes défis qu'un serveur en production destiné à être toujours actif. Les problèmes de maintenance, de coût et de performance sont nettement plus complexes avec un serveur en ligne.
- **Gestion de la Charge :** Assurer la stabilité du serveur face à un nombre potentiellement élevé de connexions simultanées nécessite une infrastructure robuste et une planification méticuleuse.

**Solutions proposées :**
- **Utilisation de Services Cloud :** Adopter une solution de serveur cloud telle qu'Amazon AWS, Microsoft Azure ou Google Cloud Platform. Ces services offrent des options évolutives et fiables pour héberger des serveurs de jeux, avec la capacité de gérer des charges de trafic fluctuantes et de maintenir une haute disponibilité.
