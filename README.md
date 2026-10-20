# lms_theme

Thème vidiSI pour [Frappe LMS](https://github.com/frappe/lms). Il personnalise l'apparence sans modifier l'app `lms` : les mises à jour de LMS restent possibles.

## Ce que fait l'app

- **Couleurs et police** : `lms_theme/public/css/lms_theme.css` redéfinit les variables de frappe-ui (bleu `#2B3480`, vert `#6CBCA0`, titres en Poppins). Le bouton « Suivant » des leçons, le menu actif, les cartes de cours et les barres de progression sont mis en valeur.
- **Injection du CSS** : `lms_theme/theme.py` (hook `after_request`) ajoute la feuille de style aux seules pages `/lms`. Le desk (`/app`), la connexion et l'API ne sont pas touchés.
- **Logo, favicon et nom** : `lms_theme/setup.py` les enregistre dans *Website Settings* à l'installation.

## Installation

Sur un bench où `lms` est déjà installé :

    bench get-app https://github.com/<compte>/lms_theme
    bench --site <site> install-app lms_theme

Sur Frappe Cloud : *Apps* → *Add app* → ce dépôt GitHub.

## Modifier

- **Couleurs** : modifier `lms_theme/public/css/lms_theme.css`, puis recharger la page (Ctrl+F5). Aucune compilation n'est nécessaire.
- **Logo** : remplacer les images de `lms_theme/public/images/`, puis :

      bench --site <site> execute lms_theme.setup.apply_branding

  `scripts/make_square_logo.py` régénère le logo carré et le favicon à partir du logo large.

## Licences

La police Poppins est sous SIL Open Font License 1.1 (`lms_theme/public/fonts/OFL.txt`).
