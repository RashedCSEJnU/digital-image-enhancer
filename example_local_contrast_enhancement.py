import imageio.v2 as imageio
import matplotlib.pyplot as plt
from image_enhancement import enhance_image



if __name__=="__main__":
    
    # select an image
    filename = "../images/lowLightImage.jpg"

    image = imageio.imread(filename)  # load image
    
    # setting up parameters
    parameters = {}
    parameters['local_contrast'] = 4  # 4x increase in details
    parameters['mid_tones'] = 0.5
    parameters['tonal_width'] = 0.5
    parameters['areas_dark'] = 0.0  # no change in dark areas
    parameters['areas_bright'] = 0.0  # no change in bright areas
    parameters['saturation_degree'] = 2  # 2x increase in color saturation
    parameters['brightness'] = 0.0  # no change in brightness
    parameters['preserve_tones'] = False
    parameters['color_correction'] = False
    image_enhanced = enhance_image(image, parameters, verbose=False)  
    
    # # display results
    # plt.figure(figsize=(7,3))
    # plt.subplot(1,2,1)
    # plt.imshow(image, vmin=0, vmax=255)
    # plt.title('Input image')
    # plt.axis('off')
    # plt.tight_layout()
    
    plt.subplot(1,1,1)
    plt.imshow(image_enhanced, cmap='gray', vmin=0, vmax=1)
    plt.title('Increased local contrast')
    plt.axis('off')
    plt.tight_layout()
    
    plt.show()
    
