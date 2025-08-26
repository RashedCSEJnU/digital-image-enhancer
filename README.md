# Digital Image Enhancer 🖼️✨

A comprehensive Python library for advanced digital image enhancement using photometric analysis and spatial tone mapping techniques. This project implements state-of-the-art algorithms for improving image quality across various scenarios including low-light photography, medical imaging, and HDR processing.

## 🌟 Features

- **Advanced Image Enhancement**: Complete pipeline with local contrast enhancement, spatial tone mapping, and color correction
- **HDR Exposure Blending**: Intelligent fusion of multiple exposures for high dynamic range imaging
- **Photometric Mask Generation**: Robust estimation of local illumination patterns
- **Medical Image Processing**: Specialized enhancement for X-rays and medical imagery
- **Color Space Management**: Proper handling of sRGB and linear color spaces
- **Flexible Parameter Control**: Fine-tuned control over enhancement parameters

## 🎯 Applications

- **Photography**: Low-light image enhancement, dynamic range expansion
- **Medical Imaging**: X-ray enhancement, contrast improvement for diagnostic images
- **Computer Vision**: Preprocessing for better feature detection and analysis
- **Content Creation**: Professional photo editing and restoration
- **Research**: Academic applications in image processing and computer vision

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/RashedCSEJnU/digital-image-enhancer.git
cd digital-image-enhancer

# Install required dependencies
pip install numpy matplotlib scikit-image imageio
```

### Basic Usage

```python
import imageio.v2 as imageio
from image_enhancement import enhance_image

# Load an image
image = imageio.imread('images/lowLightImage.jpg')

# Define enhancement parameters
parameters = {
    'local_contrast': 1.2,      # Enhance local details
    'mid_tones': 0.5,           # Midtone adjustment
    'areas_dark': 0.7,          # Dark area enhancement
    'areas_bright': 0.5,        # Bright area enhancement
    'brightness': 0.1,          # Overall brightness
    'saturation_degree': 1.2,   # Color saturation
    'color_correction': True    # Apply color correction
}

# Enhance the image
enhanced_image = enhance_image(image, parameters, verbose=True)
```

## 📂 Project Structure

```
digital-image-enhancer/
├── image_enhancement.py           # Core enhancement algorithms
├── example_enhance_image.py       # Complete enhancement pipeline
├── example_blend_exposures.py     # HDR exposure blending
├── example_medical_image.py       # Medical image processing
├── example_color_correction.py    # Color correction demo
├── example_adjust_image_brightness.py  # Brightness adjustment
├── example_local_contrast_enhancement.py  # Contrast enhancement
├── images/                        # Sample images and test cases
│   ├── lowLightImage.jpg         # Low-light photography samples
│   ├── xray.jpg                  # Medical imaging examples
│   ├── exposures_*.jpg           # HDR exposure sequences
│   └── ...                       # Various test images
└── README.md                     # This file
```

## 🔧 Core Algorithms

### 1. Photometric Mask Generation

- **Purpose**: Estimates local illumination patterns in images
- **Technique**: Robust recursive envelope filtering with sigmoid functions
- **Applications**: Spatial tone mapping, local contrast enhancement

### 2. Spatial Tone Mapping

- **Purpose**: Intelligent brightness and contrast adjustment based on local content
- **Features**: Separate processing for dark and bright regions
- **Benefits**: Preserves natural appearance while enhancing visibility

### 3. Local Contrast Enhancement

- **Purpose**: Amplifies fine details while preserving overall image structure
- **Method**: Detail extraction and selective amplification
- **Use Cases**: Medical imaging, low-light photography

### 4. HDR Exposure Blending

- **Purpose**: Combines multiple exposures into a single high-quality image
- **Algorithm**: Membership function-based weighted blending
- **Output**: Balanced exposure with enhanced dynamic range

## 📸 Example Use Cases

### Low-Light Photography Enhancement

```python
from image_enhancement import enhance_image
import imageio.v2 as imageio

image = imageio.imread('images/lowLightImage.jpg')
parameters = {
    'local_contrast': 1.5,
    'areas_dark': 0.8,
    'brightness': 0.2,
    'saturation_degree': 1.3
}
enhanced = enhance_image(image, parameters, verbose=True)
```

### Medical Image Processing

```python
from image_enhancement import apply_local_contrast_enhancement, get_photometric_mask

# Load X-ray image
xray = imageio.imread('images/xray.jpg')
mask = get_photometric_mask(xray)
enhanced_xray = apply_local_contrast_enhancement(xray, mask, degree=2.0)
```

### HDR Processing

```python
from image_enhancement import blend_expoures
import glob

# Load exposure sequence
exposures = [imageio.imread(f) for f in glob.glob('images/exposures_*.jpg')]
hdr_result = blend_expoures(exposures, threshold_dark=0.3, threshold_bright=0.7)
```

## 🎛️ Parameter Guide

| Parameter           | Range    | Description                   | Recommended Values       |
| ------------------- | -------- | ----------------------------- | ------------------------ |
| `local_contrast`    | 0.5-3.0  | Detail enhancement strength   | 1.2-1.5 for photos       |
| `mid_tones`         | 0.0-1.0  | Midtone brightness target     | 0.5 (neutral)            |
| `areas_dark`        | 0.0-1.0  | Dark region enhancement       | 0.6-0.8 for low-light    |
| `areas_bright`      | 0.0-1.0  | Bright region enhancement     | 0.3-0.5 typical          |
| `brightness`        | -1.0-1.0 | Overall brightness adjustment | ±0.1-0.3                 |
| `saturation_degree` | 0.5-2.0  | Color saturation multiplier   | 1.1-1.3 for natural look |

## 🔬 Technical Details

- **Color Space**: Supports both sRGB and linear RGB processing
- **Data Types**: Float64 precision for accurate computations
- **Image Formats**: Compatible with common formats (JPEG, PNG, TIFF)
- **Dependencies**: NumPy, SciPy, scikit-image, Matplotlib, ImageIO

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest new features.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 📚 References

This implementation is based on advanced image processing techniques including:

- Photometric stereo and shape-from-shading principles
- Multi-scale image analysis
- Perceptually-based tone mapping
- HDR imaging and exposure fusion techniques

## 📞 Contact

For questions, suggestions, or collaborations, please open an issue on GitHub.

---

_Enhance your images with professional-quality algorithms! 🚀_
