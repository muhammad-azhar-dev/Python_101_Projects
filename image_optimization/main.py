from PIL.Image import Image as Img, Transpose
from PIL import Image
import PIL.ImageFilter as ImageFilter
import PIL.ImageOps as ImageOps
import PIL.ImageEnhance as ImageEnhance

def crop_image(image:Img, start_x, start_y, end_x, end_y):
    return image.crop((start_x, start_y, end_x, end_y))

def resize_image(image:Img, width, height):
    return image.resize((width, height))

def flip_image(image:Img):
    return image.transpose(Transpose.FLIP_LEFT_RIGHT)

def rotate_image(image:Img, degrees):
    return image.rotate(degrees)

def compress_image(image:Img, save_path, quality):
    return image.save(save_path, optimize=True, quality=quality)

def blur_image(image:Img):
    return image.filter(ImageFilter.BLUR)

def sharpen_image(image:Img):
    return image.filter(ImageFilter.SHARPEN)

def adjust_brightness(image:Img, brightness):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(brightness)

def adjust_contrast(image:Img, contrast):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(contrast)

def add_filters(image:Img):
    image = ImageOps.grayscale(image)
    image = ImageOps.invert(image)
    image = ImageOps.posterize(image, 4)
    return image

def optimize_image(image:Img):
        # this will remove 500px from top
    # image = crop_image(image, 0, 500, 1200, 1600)
    # image = resize_image(image, 200, 200)
    # image = flip_image(image)
    # image = rotate_image(image, 90)
    # image = blur_image(image)
    # image = sharpen_image(image)
    # image = adjust_brightness(image, 1.6)
    # image = adjust_contrast(image, 1.6)
    image = add_filters(image)

    return image

im = Image.open('azhar.jpg')
optimized_image = optimize_image(im)
optimized_image.save('image.jpg')

# compress image
# compress_image(im, 'compressed.jpg', 10)