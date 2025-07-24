import imageio.v2 as imageio
import matplotlib.pyplot as plt
from image_enhancement import enhance_image


def load_image(filename):
    """Load an image from a specified filename."""
    try:
        image = imageio.imread(filename)
        return image
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the image: {e}")
        return None


def enhance_image_with_params(image, params):
    """Enhance the image using the specified parameters."""
    return enhance_image(image, params, verbose=False)


def display_images(original, enhanced):
    """Display the original and enhanced images side by side."""
    plt.figure(figsize=(10, 5))

    # # Original Image
    # plt.subplot(1, 2, 1)
    # plt.imshow(original, vmin=0, vmax=255)
    # plt.title('Input Image')
    # plt.axis('off')

    # Enhanced Image
    plt.subplot(1, 1, 1)
    plt.imshow(enhanced, vmin=0, vmax=255)
    plt.title('Adjusted Image Brightness')
    plt.axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Select an image
    filename = "../images/lowLightImage.jpg"

    # Load image
    image = load_image(filename)

    if image is not None:
        # Setting up parameters for enhancement
        parameters = {
            'local_contrast': 1.0,  # No increase in details
            'mid_tones': 0.5,  # Middle of range
            'tonal_width': 0.5,  # Middle of range
            'areas_dark': 0.0,  # No change in dark areas
            'areas_bright': 0.0,  # No change in bright areas
            'saturation_degree': 1.0,  # No change in color saturation
            'brightness': 0.5,  # Increase overall brightness by 50%
            'preserve_tones': True,
            'color_correction': True
        }

        # Enhance image
        image_enhanced = enhance_image_with_params(image, parameters)

        # Display results
        display_images(image, image_enhanced)
