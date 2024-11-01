# pip install pillow

from PIL import Image, ImageDraw, ImageFont

img = Image.open("meme/robotnik.jpg")           # Image à modifier
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("impact.ttf", 50)     # Police d'écriture et taille
draw.text(xy = (10, 100),                       # Emplacement du texte
    text = "Hello, World !",                    # Texte à écrire
    font=font,                                  # Police d'écriture à utiliser
    fill=(0, 0, 0)                              # Couleur du texte (noir)
)
img.save("généré/meme-1.jpg")                   # Sauvegarde de l'image
