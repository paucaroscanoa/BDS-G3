from PIL import Image, ImageFont, ImageDraw

image= Image.open('tasa.JPG')
print(image.size)
print(image.mode)
print(image.format)

#convertir imagen black - wite
#image_blackwhite=image.convert('L')
#image_blackwhite.show()

#Redimensionar una imagen
width=image.size[0]
height=image.size[1]
print(f'ancho:{width}')
print(f'alto:{height}')

new_width=width//5
new_height=height//5
print(f'nuevo ancho:{new_width}')
print(f'nuevo alto:{new_height}')

#redimensión del la imagen
new_size=(new_width,new_height)
image_short=image.resize(new_size)
#image_short.show()

#Guardar imagen
#image.save('tasa_short.jpg','JPEG',quality=90)


#Incrustar un texto a la imagen
font =ImageFont.truetype('Roboto-Bold.ttf',90)
draw = ImageDraw.Draw(image_short)
draw.text((10,0),"Mario Paucar Oscanoa",font=font)
image_short.show()
image_short.save('tasa_short_text.jpg','JPEG',quality=100)
