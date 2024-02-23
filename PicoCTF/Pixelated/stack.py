import numpy as np 
from PIL import Image

imgo = Image.open('scrambled1.png')
imgs = Image.open('scrambled2.png')
onp = np.array(imgo)*1079
snp = np.array(imgs)*1079

value = np.bitwise_xor(onp, snp).astype(np.uint8)
Image.fromarray(value).save('flag.png')
