# <center>Sujet Couralafac - TP Manipulations d'images en Python</center>

<center>Durée : 1h30</center>
<center>Ce TP n'est PAS noté</center>

Le sujet porte sur la manipulation d'images avec Python.
Pour ce faire, vous allez créer un générateur de mèmes à l'aide de la bibliothèque Pillow (abrégée PIL).

Le TP est divisé en deux parties.
Vous devriez avoir le temps d'entamer la seconde partie au bout de l'heure et demie.

Ce n'est pas grave si vous n'avez pas eu le temps de tout finir.

## Partie 1)

Durant cette partie, vous allez devoir concevoir la structure du générateur.
Prenez d'abord connaissance du dossier `/meme`, et choisissez votre mème préféré.

Une fois choisi, commencez votre générateur. Il doit permettre de créer le mème que vous avez sélectionné.

les consignes sont les suivantes :

- Une seule template doit être disponible
- On doit pouvoir choisir le texte pour chaque élément du mème
- L'utilisateur doit pouvoir configurer son mème (choisir le texte) depuis le terminal
- Le mème doit être sauvegardé dans le dossier `généré`.
- Le nom du fichier généré est libre

Voici un exemple :

````
* Meme  : Robotnik Button *
Texte bouton rouge :
> Passer une heure et demie à faire autre chose que le TD
> Texte bouton bleu :
> >>> Faire le TD proposé sur les memes parce qu'il est un peu cool
> Texte Robotnik :
> >>> Les lycéens
> ==================
> Meme généré dans /généré/meme-1.png
> ```
````

`/généré/meme-1.png` :

<center>

![img.png](https://files.voltis.cloud/TfxziP4ytzNf6brfziIOMyCFaLQGg4Zi.webp)

</center>

## Partie 2)

Une fois que le générateur fonctionne, ajoutez, dans l'ordre que vous souhaitez, les fonctionnalités suivantes :

- La possibilité de faire d'autres mèmes (utilisez ceux dans `/image`). Attention à bien placer le texte !
- Ajouter une bordure noire autour du texte
- Faire en sorte que le texte ne soit pas "trop gros", reste dans une zone déterminée (quitte à l'écrire sur plusieurs lignes ou en plus petit)
- Faire en sorte qu'une fois généré, le mème soit ouvert dans la visionneuse de photos Windows
- Choisir le format de l'image générée (png, jpg, etc)
- Créer une interface graphique

Toutes les fonctionnalités ne sont pas forcément compliquées. Certaines sont même faisable en une ligne.

## Aide

Voici un code basique pour vous dépanner :

````python
> from PIL import Image, ImageDraw, ImageFont
>
> img = Image.open("meme/robotnik.jpg")       # Image à modifier
> draw = ImageDraw.Draw(img)
> font = ImageFont.truetype("impact.ttf", 50) # Police d'écriture et taille
>
> draw.text(xy = (10, 100),                   # Emplacement du texte
>           text = "Hello, World !",          # Texte à écrire
>           font=font,                        # Police d'écriture à utiliser
>           fill=(0, 0, 0)                    # Couleur du texte (noir)
>           )
>
> img.save("généré/meme-1.jpg")               # Sauvegarde de l'image
>
> ```
````
