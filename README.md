# Photo Booth Simulation System

A Python-based photo booth application with decorative frames and passport photo functionality, built using OpenCV and computer vision technologies.

## 📋 Overview

Digital photo booth with two modes: fun photos with decorative frames and professional passport photos with AI background removal. Developed for Multimedia Systems at Università di Napoli Federico II.

## 🗂️ Project Structure

```
ProgrammaDiSimulazione/
├── main.py                    # Main application
├── cornice_1-6.png           # Decorative frames (6 options)
├── griglia.png               # Grid overlay
├── taglia_qui.png            # Cut indicator
└── README.md                 # Documentation
```

## 🎯 Key Features

### Dual Photo Modes
- **Fun Photos (Mode 0)**: 6 decorative frame options
- **Passport Photos (Mode 1)**: AI background removal with white background

### Processing Features
- Real-time camera capture with positioning grid
- MediaPipe SelfiSegmentation for background removal
- Gamma correction for brightness adjustment
- 2x2 grid layout with timestamps
- Automatic cropping to passport dimensions (400x320px)

## 🛠️ Technical Stack

- **OpenCV**: Image processing and camera capture
- **CVZone**: SelfiSegmentation integration
- **NumPy**: Array operations
- **MediaPipe**: AI segmentation

### Key Implementation

```python
# Camera setup
camera = cv.VideoCapture(1)
camera.set(cv.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

# Background removal
from cvzone.SelfiSegmentationModule import SelfiSegmentation
segmentor = SelfiSegmentation()
imgOut = segmentor.removeBG(img, (255, 255, 255), threshold=0.8)

# Gamma correction
def gamma_correction(image, gamma):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 
                     for i in np.arange(0, 256)]).astype("uint8")
    return cv.LUT(image, table)
```

## 🚀 Getting Started

### Prerequisites
```bash
pip install opencv-python numpy cvzone mediapipe
```

### Installation & Usage
1. Download project files to same directory
2. Ensure camera is connected
3. Run: `python main.py`
4. Select mode (0=fun, 1=passport)
5. For fun mode: press 1-6 to select frames
6. Press SPACE to capture 4 photos
7. Adjust gamma if needed
8. Save with custom filename

### Camera Configuration
If camera doesn't work, modify line 13:
```python
camera = cv.VideoCapture(0)  # Try 0 for built-in camera
```

## 📈 Usage Flow

### Fun Photos
1. Select mode 0 → Choose frame (keys 1-6) → Position using grid → Capture 4 photos → Adjust gamma → Save

### Passport Photos  
1. Select mode 1 → Position centrally → Capture 4 photos → Select best → Adjust gamma → Save

## 🔧 Features

- **Gamma Correction**: <1.0 brightens, >1.0 darkens
- **Output**: 2x2 grid layout with timestamp and cutting guides
- **Formats**: PNG with transparency support

## 🔍 Troubleshooting

1. **Camera issues**: Check camera index in `main.py` line 13
2. **Missing files**: Ensure all PNG assets are present
3. **Poor segmentation**: Improve lighting conditions

## 📝 Academic Context

**Author**: Federica Del Vecchio (N46004430)  
**Course**: Sistemi Multimediali  
**Institution**: Università degli Studi di Napoli "Federico II"  
**Year**: 2022  
**Language**: Python 3.x

Demonstrates computer vision, AI integration, and real-time image processing for multimedia systems education.
   python main.py
   ```

### Camera Configuration
If the default camera index doesn't work, modify line 13 in `main.py`:
```python
camera = cv.VideoCapture(0)  # Try 0 for built-in camera
```

## 📈 Usage Examples

### Fun Photo Session
1. **Launch application** and select mode `0`
2. **Choose frame** by pressing number keys (1-6) while previewing options
3. **Position yourself** using the grid overlay for optimal framing
4. **Capture 4 photos** by pressing `SPACE` key
5. **Adjust brightness** by setting gamma value (0.5-2.0 recommended)
6. **Save with custom filename**

### Passport Photo Session
1. **Launch application** and select mode `1`
2. **Position yourself** centrally within the grid overlay
3. **Capture 4 photos** by pressing `SPACE` key
4. **Select best photo** from the 4 captured images
5. **Adjust gamma** for optimal lighting (passport photos require even lighting)
6. **Save professional layout** with timestamp

### Example Output Structure
```
Final Image Layout (2x2 Grid):
┌─────────────┬─────────────┐
│   Photo 1   │   Photo 2   │
├─────────────┼─────────────┤
│   Photo 3   │   Photo 4   │
└─────────────┴─────────────┘
    Timestamp: DD/MM/YYYY HH:MM
    [Cut Here Indicator]
```

## 🔧 Advanced Features

### Gamma Correction Options
- **Gamma < 1.0**: Brightens the image (recommended: 0.7-0.9)
- **Gamma = 1.0**: No change to original brightness
- **Gamma > 1.0**: Darkens the image (recommended: 1.1-1.5)

### Background Removal Parameters
- **Threshold**: 0.8 (adjustable for different lighting conditions)
- **Background Color**: White (255, 255, 255) for passport photos
- **Edge Smoothing**: Automatic blur application for professional appearance

### Frame Overlay System
- **Dynamic loading**: Frames loaded based on user selection
- **Transparent overlay**: PNG alpha channel support
- **Proportional scaling**: Maintains aspect ratio during application

## 📚 File Output Specifications

### Passport Photos
- **Dimensions**: 400x320 pixels per photo
- **Background**: Pure white with edge blur
- **Layout**: 2x2 grid with white borders
- **Metadata**: Timestamp and cutting guides

### Fun Photos
- **Dimensions**: Variable based on frame selection
- **Background**: Original or frame-integrated
- **Layout**: 2x2 grid with decorative elements
- **Metadata**: Timestamp and cutting guides

---

**Author**: Federica Del Vecchio (N46004430)  
**Course**: Sistemi Multimediali  
**Institution**: Università degli Studi di Napoli "Federico II"  
**Academic Year**: 2022  
