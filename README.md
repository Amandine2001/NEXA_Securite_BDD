# NEXA_Securite_BDD

## Contexte

Dans le cadre de ce projet sur la sécurité des données, l'entreprise DataSecure Inc., spécialisée dans la gestion de données sensibles dans le secteur financier, souhaite mettre en place un système de chiffrement et de sauvegarde des données afin de renforcer leur sécurité.

Pour répondre à leur besoin, une solution Python devra être capable de chiffrer les données avant de les sauvegarder, en comparant ainsi les méthodes de chiffrement symétrique et asymétrique, et de mettre en place un système de sauvegarde de ces données dans deux localisations différentes. De plus, cette solution devra fonctionner pour des fichiers en format Excel (.xlsx), CSV (.csv) et texte (.txt).

## Explication du fonctionnement du programme

### 1. Vérification du format du document

Le module `check_format.py`permet à l'aide de la fonction `check_format_doc(chemin_fichier)` de vérifier le format du document qui est utilisé en rentrant comme argument le chemin du fichier (*str*). Cela permet ainsi d'être sûr de n'avoir que des fichiers au format Excel (.xlsx), CSV (.csv) et texte (.txt), sinon le programme retourne une erreur signalant que le format du document donné n'est pas compatible.

### 2. Lecture du document 

En fonction du type de document, le programme va lire le contenu du fichier en faisant appel au module `lecture_fichier`. Une fonction est dédiée pour chacun des trois types de document (`lecture_fichier_txt(chemin_fichier)`, `lecture_fichier_csv(chemin_fichier)`, `lecture_fichier_xlsx(chemin_fichier)`). Cela permet d'avoir une visualisation directe du contenu du fichier en un format exploitable et lisible à l'aide de Python.

### 3. Gestion des clés de chiffrement 

Le module `gestion_cle.py` permet de créer et de lire les clés de chiffrement. 
Pour le chiffrement symétrique, la fonction `generation_cle_fernet(key_path)` permet de créer la clé et `lecture_cle_fernet(key_path)`. 

### 3. Chiffrement et déchiffrement du document de façon symétrique

Pour la partie sur le chiffrement symétrique, le module `chiffrement_symetrique.py` y est dédié contenant une fonction pour l'encodage `chiffrement_symetrique(input_path, key, output_path)` et une fonction pour le décodage `dechiffrement_symetrique(input_path, key, output_path)`. 

Celle pour l'encodage vérifie l'existance du fichier depuis le chemin d'accès et crée le nom d'un fichier de sortie en y ajoutant l'extension *.enc*, signalant le fait que cela soit un fichier crypté. La fonction lit sous forme de bytes le fichier, crypte les données à l'aide de Fernet (une méthode de cryptographie à clé secrète symétrique - AES) et l'écrit sous forme de bytes dans le nouveau fichier dédié à la sauvegarde de l'encodage.

De même pour la fonction de déchiffrement, c'est le chemin inverse en prenant le fichier encodé comme entrée qu'il faut décrypter à l'aide de la clé générée pour l'encodage. En sortie, c'est le contenu du fichier initial mais en format *str* qui est sauvegardé.

En résumé, le chiffrement symétrique utilise donc une seule clé pour chiffrer et déchiffrer les données, ce qui le rend très rapide mais pose un problème pour transmettre la clé de manière sécurisée.

### 4. Chiffrement et déchiffrement du document de façon asymétrique

Pour la partie sur le chiffrement asymétrique, l'utilisation d'une paire de clés (publique et privée) permet un échange sécurisé, mais il est beaucoup plus lent et peu adapté aux fichiers.

En effet, en testant le modèle de chiffrement RSA seul (`chiffrement_test_rsa.py`), ce dernier ne supporte pas vraiment les fichiers (même 15Ko est lourd et stop le code). 

Cette méthode n'est pas active dans le `main.py`car cela génère une erreur.  


### 5. Chiffrement et déchiffrement du document de façon hybride

La création d'un module hybride est préférable pour répondre au problème énoncé précedemment afin d'avoir le fichier chiffré avec un algorithme symétrique rapide (ici Fernet) et c'est la clé de chiffrement qui est chiffrée de façon asymétrique (RSA) permettant de sécuriser l'échange. Cette approche offre donc à la fois la rapidité du symétrique et la sécurité de l’asymétrique, ce qui en fait la solution la plus efficace dans le cas présenté.

Le module hybride est nommé `chiffrement_asymetrique.py`. Ce dernier contient une fonction pour l'encodage `encrypt_file_hybrid(input_path, public_key_path)` et une fonction pour le décodage `decrypt_file_hybrid(input_path, private_key_path)`. 

Celle pour l'encodage fait un chiffrement symétrique à l'aide de Fernet puis une fois que la clé est crée, l'algorithme la chiffre de façon asymétrique (RSA). Cela permet ainsi une sécurisation à la fois du texte avec le chiffrement symétrique qui est plus adapté aux fichiers et de la clé de chiffrement grâce à la méthode RSA.

### 7. Sauvegarde des chiffrements

Création d'un module `sauvegarde.py` permettant à l'aide de la fonction `sauvegarde_fichier(source_path, destination1, destination2)` d'enregistrer dans deux dossiers différents les fichiers cryptés.

## Le détail des tests réalisés pour choisir la bonne méthode de chiffrement

Pour choisir la bonne méthode de chiffrement, 

## Description des tests réalisés pour vérifier le fonctionnement de la méthode de sauvegarde.

Les tests des fonctions ont été réalisés avec quatre fichiers (format .txt, .csv, .xlsx et .docx) pour vérifier que l'algorithme supporte correctement les trois formats imposés, à savoir .txt, .csv et .xlsx, et repère également lorsque le fichier à chiffrer ne correspond pas au bon formatage, en l'occurence avec un .docx. 

De plus, les fonctions de déchiffrement permettent de vérifier si le chiffrement a été correctement réalisé par la fonction d'encodage et que le fichier chiffré sauvegardé soit correctement lu.

## Les instructions pour l'exécution du script

- `git clone https://github.com/Amandine2001/NEXA_Securite_BDD.git` dans le terminal de VS Code ;
- `cd NEXA_Securite_BDD` pour se positionner dans le dossier contenant le code ;
- `python -m venv venv`pour la création de l'environnement virtuel ;
- `venv\Scripts\Activate` permet d'activer l'environnement virtuel ;
- `pip install -r requirements.txt` pour installer les librairies utilisées ;
- `config.properties`correspond au fichier où l'on va stocker le chemin du fichier que l'on souhaite chiffrer (`NOM_FICHIER_A_CHIFFRE`) et le chemin pour les dossiers de sauvegarde (`NOM_DOSSIER_SAUVEGARDE_LOCALE`, `NOM_DOSSIER_SAUVEGARDE_CLOUD`) pour ainsi permettre à l'algorithme d'être le plus flexible possible sans venir le modifier ;
- `python main.py` permet de lancer l'algorithme une fois que le chemin du fichier est mis dans le fichier `config.properties` comme indiqué précedemment.
