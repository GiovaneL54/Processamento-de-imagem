from image_processor import  apply_filter, resize_image



#Aplicando o filtro
image = apply_filter('C:/Users/Giovane/Downloads/Pandas/florestas vermelhas.jpg', 'BLUR')
image.show()

#Redimencionando a imagem
resize_image = resize_image('C:/Users/Giovane/Downloads/Pandas/florestas vermelhas.jpg', 200,200)
resize_image.show()