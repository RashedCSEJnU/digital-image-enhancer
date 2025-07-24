import imageio.v2 as imageio
import matplotlib.pyplot as plt
from skimage import img_as_float, img_as_ubyte
from image_enhancement import correct_colors  # assuming correct_colors is defined in this module

if __name__ == "__main__":
    # Select an image
    filename = "../images/lowLightImage.jpg"
    image = imageio.imread(filename)  # load image

    # Convert image to float range [0,1] for processing if it's not already
    image_float = img_as_float(image)

    # Apply color correction
    image_enhanced = correct_colors(image_float, verbose=False)

    # Convert enhanced image back to [0,255] for display
    image_enhanced_ubyte = img_as_ubyte(image_enhanced)

    # Display results
    # plt.figure(figsize=(10, 5))
    # plt.subplot(1, 2, 1)
    # plt.imshow(image)
    # plt.title('Input Image')
    # plt.axis('off')

    plt.subplot(1, 1, 1)
    plt.imshow(image_enhanced_ubyte)
    plt.title('Color Corrected Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
