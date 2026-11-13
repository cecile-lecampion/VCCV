"""
Fabrique les images allégées du site à partir des fichiers originaux.

Ce script est lancé automatiquement par GitHub à chaque publication du site.
Vous pouvez aussi le lancer sur votre Mac pour voir les nouvelles images
dans l'aperçu local (mkdocs serve) :

    python3 outils/images_site.py

Fonctionnement : pour chaque ligne du tableau IMAGES ci-dessous, l'original
(à gauche) est réduit et enregistré dans docs/images/ (à droite).
Si vous renommez ou déplacez un original, mettez à jour sa ligne ici.
Si un original est introuvable, le script le signale et garde l'ancienne copie.

Les photos de la galerie ne sont PAS traitées ici : elles sont choisies
à la main (droit à l'image), voir docs/galerie.md.
"""

from pathlib import Path
from PIL import Image, ImageOps

RACINE = Path(__file__).resolve().parent.parent
SORTIE = RACINE / "docs" / "images"

# original (depuis la racine du dépôt) : (copie dans docs/images, taille max en pixels)
IMAGES = {
    # --- Super Chloro -------------------------------------------------------
    "Super_Chloroplaste/SC_Vector.png": ("persos/super-chloro.png", 700),
    "Super_Chloroplaste/SC_Bagette_Vector.png": ("persos/super-chloro-baguette.png", 900),
    "Super_Chloroplaste/SC_affaibli_Vector.png": ("persos/super-chloro-affaibli.png", 500),
    "Super_Chloroplaste/SC_bricoleur_Vector.png": ("persos/super-chloro-bricoleur.png", 500),
    # --- Logos des publics --------------------------------------------------
    "Autres_acteurs/symbole_niveaux/plante_niveau_1.png": ("niveaux/niveau-1.png", 160),
    "Autres_acteurs/symbole_niveaux/plante_niveau_2.png": ("niveaux/niveau-2.png", 160),
    "Autres_acteurs/symbole_niveaux/plante_niveau_3.png": ("niveaux/niveau-3.png", 160),
    # --- Monstres -----------------------------------------------------------
    "Autres_acteurs/monstres/faible lumiere.png": ("monstres/faible-lumiere.png", 360),
    "Autres_acteurs/monstres/forte_lumiere.png": ("monstres/forte-lumiere.png", 360),
    "Autres_acteurs/monstres/secheresse.png": ("monstres/secheresse.png", 360),
    "Autres_acteurs/monstres/chaleur.png": ("monstres/chaleur.png", 360),
    "Autres_acteurs/monstres/carence.png": ("monstres/carence.png", 360),
    "Autres_acteurs/monstres/obscurite.png": ("monstres/obscurite.png", 360),
    # --- Cartes : dos des trois paquets -------------------------------------
    "Carte/cartes_vierges/carte_A5_Stress_recto.png": ("cartes/dos-stress.jpg", 520),
    "Carte/cartes_vierges/carte_A5_Consequence_recto.png": ("cartes/dos-consequence.jpg", 520),
    "Carte/cartes_vierges/carte_A5_Reponse cellule_recto.png": ("cartes/dos-reponse.jpg", 520),
    # --- Cartes : exemples affichés sur la page « Les cartes » --------------
    "Carte/cartes_stress/forte_lumiere.png": ("cartes/stress-forte-lumiere.jpg", 520),
    "Carte/cartes_consequences/ox.png": ("cartes/consequence-oxydation.jpg", 520),
    "Carte/cartes_reponses/dissipation chaleur.png": ("cartes/reponse-dissipation.jpg", 520),
}


def alleger(original: Path, copie: Path, taille_max: int) -> None:
    image = ImageOps.exif_transpose(Image.open(original))
    image.thumbnail((taille_max, taille_max), Image.LANCZOS)
    copie.parent.mkdir(parents=True, exist_ok=True)
    if copie.suffix.lower() in (".jpg", ".jpeg"):
        image.convert("RGB").save(copie, quality=82, optimize=True, progressive=True)
    else:
        image.save(copie, optimize=True)


def main() -> None:
    manquants = 0
    for chemin_original, (chemin_copie, taille_max) in IMAGES.items():
        original = RACINE / chemin_original
        if not original.exists():
            print(f"ATTENTION : original introuvable, ancienne copie conservée : {chemin_original}")
            manquants += 1
            continue
        alleger(original, SORTIE / chemin_copie, taille_max)
    print(f"{len(IMAGES) - manquants} image(s) mise(s) à jour, {manquants} introuvable(s).")


if __name__ == "__main__":
    main()
