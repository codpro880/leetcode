import numpy as np

def flip_img(img):
    img = np.array(img)
    img_rev = img[:, ::-1]
    img_flip = img_rev ^ img_rev
    return img_rev

if __name__ == "__main__":
    img = [[1, 1, 0], [0,0,1], [0, 0, 0]]
    print(flip_img(img))
