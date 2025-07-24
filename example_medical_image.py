import imageio.v2 as imageio  # Use v2 to avoid the deprecation warning
import matplotlib.pyplot as plt
from skimage.util import img_as_float
from skimage.color import rgb2gray

from image_enhancement import get_photometric_mask
from image_enhancement import apply_spatial_tonemapping
from image_enhancement import apply_local_contrast_enhancement

if __name__ == "__main__":
    # Select an image
    filename = "../images/xray.jpg"

    # Load the image
    image = imageio.imread(filename)

    # Check if the image has 3 channels (i.e., RGB) before converting to grayscale
    if image.ndim == 3:
        image = rgb2gray(image)

    # Convert to float format for processing
    image = img_as_float(image)

    # Get estimation of the local neighborhood
    image_ph_mask = get_photometric_mask(
        image=image,
        verbose=False
    )

    # Increase the local contrast of the grayscale image
    image_contrast = apply_local_contrast_enhancement(
        image=image,
        image_ph_mask=image_ph_mask,
        degree=2,  # x2 local details
        verbose=False
    )

    # Apply spatial tonemapping on the previous stage
    image_tonemapped = apply_spatial_tonemapping(
        image=image_contrast,
        image_ph_mask=image_ph_mask,
        mid_tone=0.5,
        tonal_width=0.5,
        areas_dark=0.0,  # no improvement in dark areas
        areas_bright=0.8,  # strong improvement in bright areas
        preserve_tones=False,
        verbose=False
    )

    # Display results
    plt.figure(figsize=(7, 3))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray', vmin=0, vmax=1)
    plt.title('Input Image')
    plt.axis('off')
    plt.tight_layout()

    plt.subplot(1, 2, 2)
    plt.imshow(image_tonemapped, cmap='gray', vmin=0, vmax=1)
    plt.title('Enhanced Image')
    plt.axis('off')
    plt.tight_layout()

    plt.show()
