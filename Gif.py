import os
import imageio

myfile = os.listdir('images_1')
images = []
for i in range(len(myfile)):
    image = imageio.imread('images_1/' + myfile[i])
    images.append(image)

imageio.mimsave('My daughter Kimia painting.gif' , images)
print('conver is Finished')