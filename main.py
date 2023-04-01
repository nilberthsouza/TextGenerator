import cv2

# carrega a imagem
img = cv2.imread('C:\\Users\\nilbe\\Downloads\\cut\\letrasmaiusculas.png')

# divide a imagem em 4 blocos verticais e 6 blocos horizontais
rows, cols, channels = img.shape
block_height = int(rows / 4)
block_width = int(cols / 6)

# corta a imagem em 24 blocos
for i in range(4):
    for j in range(6):
        y1 = i * block_height
        y2 = (i + 1) * block_height
        x1 = j * block_width
        x2 = (j + 1) * block_width
        block = img[y1:y2, x1:x2]
        cv2.imwrite(f'bloco_{i}_{j}.png', block)
