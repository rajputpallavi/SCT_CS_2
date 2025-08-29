# SCT_CS_2
💡 Task 2 Completed – PixGuard: Image Encryption Tool
As part of my internship at Skillcraft Technology, I developed PixGuard, a simple yet effective Python tool for image encryption and decryption using pixel manipulation techniques.
PixGuard demonstrates how to encrypt images by manipulating pixels directly. It supports pixel-level operations such as swapping pixel values and applying a basic mathematical operation (XOR) on each pixel for secure encryption and decryption. It is an effective image encryption tool using **pixel manipulation** techniques in Python.

## 🔐 Features

- **Swap Pixels**: Encrypts images by swapping pixels in a checkerboard pattern
- **XOR Encryption**: Applies an XOR operation on image pixels using a user-defined key (0–255)
- Supports both encryption and decryption by applying the same operation again
-**Combined Operation**: Supports combined swapping and XOR for stronger encryption.
-Both encryption and decryption are supported by applying the same operation twice.
Command-line interface (CLI) for easy user interaction with file input/output support.
- CLI-based interface with file I/O support

## 🚀 How to Run

1. Install required packages:
```bash
pip install pillow numpy
```

2. Run the script:
```bash
python PixGuard.py
```

3. Follow the on-screen prompts to:
-Choose an encryption operation (Swap, XOR, or Swap + XOR)
-Provide the input image path
-Input the XOR key if applicable
-Specify the output file path

## 🛠 Technologies Used

- Python 3
- `Pillow` for image handling
- `NumPy` for pixel-level manipulation


💼 Developed as part of my internship at **Skillcraft Technology** to strengthen skills in image processing, secure data handling, and Python programming.
