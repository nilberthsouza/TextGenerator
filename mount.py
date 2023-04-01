from PIL import Image
import string

path = "C:\\Users\\nilbe\\Downloads\\cut\\cuts\\"

width = 100
height = 100

# Cria um dicionário com as imagens das letras
images = {}
for letter in string.ascii_uppercase:
    filename = path + letter + ".png"
    images[letter] = Image.open(filename).resize((width, height))

# Define uma imagem vazia do tamanho de um espaço em branco
space_image = Image.new('RGBA', (width, height), (0, 0, 0, 0))

text = input("Digite um texto: ")

# Cria uma lista de imagens correspondentes às letras do texto
text_images = []
for letter in text.upper():
    if letter in images:
        text_images.append(images[letter])
        text_images.append(space_image)  # adiciona um espaço em branco após cada letra
    elif letter == " ":
        text_images.append(space_image)  # adiciona um espaço em branco quando o usuário digita um espaço

# Remove o espaço em branco extra no final do texto, se houver
if text_images and text_images[-1] == space_image:
    text_images.pop()

# Calcula o tamanho da imagem final
total_width = len(text_images) * width
max_height = height

# Cria uma imagem vazia do tamanho adequado
result = Image.new('RGBA', (total_width, max_height), (0, 0, 0, 0))

# Combina as imagens das letras em uma única imagem
x_offset = 0
for letter_image in text_images:
    result.paste(letter_image, (x_offset, 0))
    x_offset += width

result.save("texto.png")
