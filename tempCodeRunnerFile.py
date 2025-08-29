"""task2:-develop a simple image encryption tool using pixel manipulation support opearation like swapping pixel values or applying a basic mathematical operation to each pixel"""

from PIL import Image
import numpy as ip  

def swap_pixels(image):
    """Encrypt/decrypt by swapping pixels in a checkerboard pattern."""
    img_array = ip.array(image)
    height, width = img_array.shape[:2]

    for y in range(0, height - 1, 2):
        for x in range(0, width - 1, 2):
            img_array[y, x], img_array[y + 1, x + 1] = img_array[y + 1, x + 1].copy(), img_array[y, x].copy()
            img_array[y + 1, x], img_array[y, x + 1] = img_array[y, x + 1].copy(), img_array[y + 1, x].copy()

    return Image.fromarray(img_array)

def xor_pixels(image, key=128):
    """Encrypt/decrypt by applying XOR operation to each pixel with a key."""
    img_array = ip.array(image)
    img_array ^= key
    return Image.fromarray(img_array)

def process_image(input_image, operation, key=None):
    """Process the image based on the chosen operation."""
    if operation == 'swap':
        return swap_pixels(input_image)
    elif operation == 'xor':
        return xor_pixels(input_image, key)
    else:
        raise ValueError("Invalid operation. Choose 'swap' or 'xor'.")

def main():
    print("=== Image Encryption Tool ===")
    print("1. Swap Pixels")
    print("2. XOR Pixels")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1–3): ")

        if choice == '3':
            print("Exiting program...")
            break

        if choice in ['1', '2']:
            try:
            
                # Input image file path
                input_path = input("Enter input image path (e.g., input.png): ")
                image = Image.open(input_path).convert("RGB")  # Load and convert to RGB

                if choice == '2':
                    key = int(input("Enter XOR key (0–255): "))
                    if not 0 <= key <= 255:
                        print("Key must be between 0 and 255.")
                        continue
                else:
                    key = None

                operation = 'swap' if choice == '1' else 'xor'
                result = process_image(image, operation, key)

                # Save output image
                output_path = input("Enter output image path (e.g., output.png): ")
                result.save(output_path)
                print(f"Image processed with '{operation}' operation and saved to {output_path}.")

            except FileNotFoundError:
                print("Error: Input image file not found.")
            except Exception as e:
                print(f"Error processing image: {e}")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
