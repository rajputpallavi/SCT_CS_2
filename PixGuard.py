from PIL import Image
import numpy as np

def welcome_message():
    print("="*70)
    print("   Welcome to 'PixGuard' Your Image Encryption Tool!")
    print("="*70)
    print("\nYou can encrypt/decrypt images with:")
    print("  [1] Swap Pixels (checkerboard permutation)")
    print("  [2] XOR Pixels (bitwise value scrambling)")
    print("  [3] Swap + XOR (maximum effect)")
    print("-"*70)

def thank_you_message():
    print("\n" + "="*70)
    print("        Thank you for using the tool!")
    print("="*70 + "\n")

def swap_pixels(image):
    img_array = np.array(image)
    height, width = img_array.shape[:2]
    for y in range(0, height - 1, 2):
        for x in range(0, width - 1, 2):
            img_array[y, x], img_array[y + 1, x + 1] = img_array[y + 1, x + 1].copy(), img_array[y, x].copy()
            img_array[y + 1, x], img_array[y, x + 1] = img_array[y, x + 1].copy(), img_array[y + 1, x].copy()
    return Image.fromarray(img_array)

def xor_pixels(image, key=128):
    img_array = np.array(image)
    result = img_array ^ key
    return Image.fromarray(result)

def swap_xor_pixels(image, key=128):
    # First swap, then XOR
    swapped = swap_pixels(image)
    return xor_pixels(swapped, key)

def process_image(input_image, operation, key=None):
    if operation == 'swap':
        return swap_pixels(input_image)
    elif operation == 'xor':
        return xor_pixels(input_image, key)
    elif operation == 'swapxor':
        return swap_xor_pixels(input_image, key)
    else:
        raise ValueError("Invalid operation.")

def main():
    welcome_message()
    while True:
        print("Menu:\n [1] Swap Pixels\n [2] XOR Pixels\n [3] Swap + XOR\n [4] Exit")
        choice = input("Enter your choice (1–4): ")

        if choice == '4':
            print("Exiting program...")
            thank_you_message()
            break

        if choice in ['1', '2', '3']:
            try:
                input_path = input("Enter input image path (e.g., input.png): ")
                image = Image.open(input_path).convert("RGB")

                key = None
                if choice in ['2', '3']:
                    k = input("Enter XOR key (0–255) or press Enter for 128: ")
                    key = int(k) if k else 128
                    if not 0 <= key <= 255:
                        print("Key must be between 0 and 255.")
                        continue

                if choice == '1':
                    operation = 'swap'
                elif choice == '2':
                    operation = 'xor'
                else:
                    operation = 'swapxor'

                result = process_image(image, operation, key)

                output_path = input("Enter output image path (e.g., output.png): ")
                result.save(output_path)
                print(f"\nImage processed with '{operation}' operation and saved to '{output_path}'.")

            except FileNotFoundError:
                print("Error: Input image file not found.")
            except Exception as e:
                print(f"Error processing image: {e}")
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
