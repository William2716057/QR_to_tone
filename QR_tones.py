from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import qrcode
import winsound  # built-in on Windows, no install needed
#pip uninstall pydub

def play_tone(frequency, duration_ms=5000): #make slower
    "Play tone"
    winsound.Beep(frequency, duration_ms)
 
 
def read_qr_and_play_tones(image):
    """Read QR image pixel by pixel, low tone for black, high for white."""
    img_array = np.array(image.convert("L"))  # convert to grayscale
 
    # Sample every 10th pixel
    for row in img_array[::10]:
        for pixel in row[::10]:
            if pixel < 128:   # black
                play_tone(frequency=300, duration_ms=100)
            else:             # white
                play_tone(frequency=1000, duration_ms=100)
 
 
def qr_gen():
    input_text = input("Input text: ")
    if not input_text:
        print("No input received!")
        return
 
    qr = qrcode.QRCode(
        #greyscale here
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,
    )
 
    qr.add_data(input_text)
    qr.make(fit=True)
 
    image = qr.make_image(fill_color="black", back_color="white")
 
    plt.imshow(np.array(image))
    plt.axis('off')
    plt.show()
 
    #play_tones = input("Play tones? (y/n): ").strip().lower()
    #if play_tones == 'y':
    print("Playing tones...)")
    read_qr_and_play_tones(image)
 
  
if __name__ == "__main__":
    qr_gen()