# Mettre en place le site de l'atelier VCCV

Ce guide explique comment installer le site dans le dépôt GitHub VCCV.
Il faut compter environ 15 minutes la première fois. Ensuite, le site se met
à jour tout seul à chaque modification.

---

## 1. Copier les fichiers dans le dépôt

Le dossier fourni contient :

```
mkdocs.yml                  ← configuration du site (titre, couleurs, menu)
requirements-docs.txt       ← outils nécessaires (lu automatiquement par GitHub)
.github/workflows/site.yml  ← publication automatique
docs/                       ← le contenu du site, une page = un fichier .md
    index.md                    Accueil
    materiel.md                 Le matériel (modèles 3D)
    animer/index.md             Animer l'atelier (présentation des 3 phases)
    animer/cellule.md           Phase 1 : la cellule végétale
    animer/chloroplaste.md      Phase 2 : plongée dans le chloroplaste
    cartes.md                   Les cartes (phase 3)
    fascicule.md                Le guide de l'animateur
    galerie.md                  Galerie photos
    adapter.md                  Adapter et contribuer
    credits.md                  Qui sommes-nous ?
    images/                     images du site (versions allégées)
    stylesheets/extra.css       retouches d'apparence
```

Copiez **tout** à la racine de votre dépôt local VCCV, à côté de vos dossiers
existants, puis dans le Terminal :

```bash
cd chemin/vers/VCCV
git add mkdocs.yml requirements-docs.txt .github docs
git commit -m "Ajout du site de l'atelier"
git push
```

> ⚠️ Le dossier `.github` commence par un point : il est **caché** dans le
> Finder. Affichez les fichiers cachés avec `Cmd + Maj + .` pour le voir.
> Si votre dépôt contient déjà un dossier `docs/` utilisé pour autre chose,
> dites-le moi, on adaptera.

## 2. Activer GitHub Pages (une seule fois)

1. Sur la page du dépôt GitHub, cliquez sur **Settings**.
2. Dans le menu de gauche, cliquez sur **Pages**.
3. Sous **Build and deployment** → **Source**, choisissez **GitHub Actions**.

C'est tout. Dans l'onglet **Actions** du dépôt, vous verrez la publication
« Publier le site » tourner (rond orange), puis réussir (coche verte) en une
à deux minutes.

Le site est alors en ligne à l'adresse :
**https://cecile-lecampion.github.io/VCCV/**

## 3. Mettre l'adresse du site en évidence sur GitHub

Pour que les visiteurs qui arrivent sur GitHub trouvent le site :

- Sur la page d'accueil du dépôt, cliquez sur la roue dentée à côté de
  **About** (à droite), cochez **Use your GitHub Pages website** et enregistrez.
- Ajoutez en haut du `README.md` une ligne comme :

  ```markdown
  ## 👉 [Accéder au site de l'atelier](https://cecile-lecampion.github.io/VCCV/)
  ```

Sur les supports papier de l'atelier, donnez plutôt l'adresse du site
(ou un QR code qui pointe vers elle) que celle de GitHub.

## 4. Voir le site sur votre Mac avant de publier (facultatif)

Pratique pour vérifier une page avant de la pousser sur GitHub.
Une seule fois, dans le Terminal :

```bash
cd chemin/vers/VCCV
python3 -m venv .venv-docs
source .venv-docs/bin/activate
pip install -r requirements-docs.txt
```

Puis, à chaque fois que vous voulez prévisualiser :

```bash
cd chemin/vers/VCCV
source .venv-docs/bin/activate
mkdocs serve
```

Ouvrez **http://127.0.0.1:8000** dans votre navigateur. La page se recharge
toute seule à chaque fois que vous enregistrez un fichier. `Ctrl + C` pour
arrêter.

> Ajoutez la ligne `.venv-docs/` et la ligne `site/` à votre fichier
> `.gitignore` pour ne pas envoyer ces dossiers sur GitHub.

## 5. Modifier le contenu

> 📷 **À propos des images** : le site n'utilise que les images placées dans
> `docs/images/`. Ce sont des copies allégées (quelques centaines de Ko) des
> originaux rangés dans `Gallerie/`, `Carte/`, `Super_Chloroplaste/`, etc.,
> pour que les pages se chargent vite. Pour ajouter une photo au site,
> réduisez-la d'abord (1200 pixels de large suffisent, par exemple avec
> Aperçu : Outils → Ajuster la taille) puis déposez-la dans `docs/images/`.

Chaque page est un fichier `.md` dans `docs/`. Vous pouvez les modifier
directement sur GitHub (icône crayon ✏️) ou sur votre Mac.

### Les éléments les plus utiles

**Ajouter une image** (déposée dans `docs/images/`) :

```markdown
![Texte décrivant l'image](images/ma-photo.jpg){ width="500" }
```

Depuis une page d'un sous-dossier (par exemple `animer/`), écrivez
`../images/ma-photo.jpg`.

**Un encadré coloré** (les 4 espaces de retrait sont importants) :

```markdown
!!! tip "Astuce"
    Le texte de l'encadré.
```

Types disponibles : `note`, `tip`, `info`, `warning`, `question`, `example`,
`abstract`.

**Un encadré repliable** (pour les questions/réponses) : remplacez `!!!`
par `???`.

**Un bouton** :

```markdown
[Texte du bouton](adresse){ .md-button .md-button--primary }
```

**Des indices et exposants** : `CO~2~` donne CO₂, `H^+^` donne H⁺.

**Ajouter une page au menu** : créez le fichier `.md` dans `docs/`, puis
ajoutez une ligne dans la partie `nav:` de `mkdocs.yml`.

## 6. Proposer les fichiers en téléchargement (Releases)

Plutôt que d'envoyer les visiteurs fouiller dans les dossiers GitHub :

1. Préparez des fichiers zip : par exemple `VCCV-modele-3D.zip` (tous les STL),
   `VCCV-cartes.pdf`, `VCCV-modeles-vierges.zip`, `VCCV-fascicule.pdf`.
2. Sur GitHub : **Releases** (colonne de droite) → **Draft a new release**.
3. Donnez un numéro de version (par exemple `v1.0`), un titre, et glissez
   les fichiers dans la zone prévue.
4. **Publish release**.

Les boutons « Télécharger » du site pointent déjà vers
`…/releases/latest` : ils mènent toujours à la dernière version publiée.

Pour un lien direct vers un fichier précis (téléchargement immédiat) :

```
https://github.com/cecile-lecampion/VCCV/releases/latest/download/VCCV-modele-3D.zip
```

Le nom du fichier doit rester identique d'une version à l'autre pour que
le lien fonctionne toujours.

## 7. Pour aller plus loin

- **HAL et Software Heritage** pour rendre l'atelier citable et l'archiver
  durablement :
    1. **Le fascicule et les cartes (PDF)** se déposent dans HAL comme
       n'importe quel document, avec le type « Cours » (ou le type que
       conseille votre service de documentation). HAL leur attribue un
       identifiant pérenne `hal-XXXXXXXX`.
    2. **Le dépôt GitHub entier** (STL, sources, site) peut être archivé
       par Software Heritage : sur softwareheritage.org, rubrique
       « Save code now », collez l'adresse du dépôt GitHub. Vous obtenez
       un identifiant SWHID.
    3. **Optionnel** : déposer ce SWHID dans HAL avec le type « Logiciel »,
       pour que le dépôt apparaisse aussi dans HAL. Ce type est prévu pour
       du code ; demandez à votre correspondant HAL s'il convient à du
       matériel pédagogique.
    4. Reportez les identifiants dans la page `docs/credits.md`.
- **Zenodo** reste possible en complément si vous voulez un DOI attribué
  automatiquement à chaque Release.
- **Documentation complète du thème** :
  https://squidfunk.github.io/mkdocs-material/

## En cas de problème

Si la coche dans l'onglet **Actions** est rouge, cliquez dessus pour lire
l'erreur. Les causes les plus fréquentes :

- une image ou un lien vers un fichier qui n'existe pas (vérifiez
  l'orthographe et les majuscules du nom de fichier) ;
- un retrait incorrect dans `mkdocs.yml` (ce fichier est sensible aux espaces).
