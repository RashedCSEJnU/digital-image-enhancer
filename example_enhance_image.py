import imageio.v2 as imageio
import matplotlib.pyplot as plt
from image_enhancement import enhance_image


def load_image(filename):
    try:
        image = imageio.imread(filename)
        return image
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the image: {e}")
        return None


def display_images(original, enhanced):
    plt.figure(figsize=(10, 5))

    # Original Image
    plt.subplot(1, 2, 1)
    plt.imshow(original, vmin=0, vmax=255)
    plt.title('Input Image')
    plt.axis('off')

    # Enhanced Image
    plt.subplot(1, 2, 2)
    plt.imshow(enhanced, vmin=0, vmax=255)
    plt.title('Enhanced Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Select an image
    filename = "../images/lowLightImage.jpg"
    # filename = "../images/alhambra2.jpg"
    # filename = "../images/lisbon.jpg"

    # Load image
    image = load_image(filename)

    if image is not None:
        # Setting up parameters for enhancement
        parameters = {
            'local_contrast': 1.2,  # 1.2x increase in details
            'mid_tones': 0.5,  # Middle of range
            'tonal_width': 0.5,  # Middle of range
            'areas_dark': 0.7,  # 70% improvement in dark areas
            'areas_bright': 0.5,  # 50% improvement in bright areas
            'brightness': 0.1,  # Slight increase in overall brightness
            'saturation_degree': 1.2,  # 1.2x increase in color saturation
            'preserve_tones': True,
            'color_correction': True
        }

        # Enhance image
        image_enhanced = enhance_image(image, parameters, verbose=False)

        # Display results
        display_images(image, image_enhanced)
