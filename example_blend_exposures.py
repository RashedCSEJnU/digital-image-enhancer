import glob
import imageio.v2 as imageio
from image_enhancement import blend_expoures


def load_images_from_directory(directory_pattern):
    """Load images from a directory matching the given pattern."""
    exposure_filenames = glob.glob(directory_pattern)
    image_list = []

    for filename in exposure_filenames:
        try:
            image = imageio.imread(filename)
            image_list.append(image)
        except Exception as e:
            print(f"Error loading {filename}: {e}")

    return image_list


def main():
    # Select a collection of image exposures
    directory_pattern = '../images/exposures_A*.jpg'

    # Load the exposures into a list
    image_list = load_images_from_directory(directory_pattern)

    if image_list:  # Ensure we have loaded images
        # Blend exposures
        exposure_blend = blend_expoures(
            image_list,
            threshold_dark=0.35,
            threshold_bright=0.65,
            verbose=True
        )
    else:
        print("No images were loaded. Please check the directory and patterns.")


if __name__ == "__main__":
    main()
