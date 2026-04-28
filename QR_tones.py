from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import qrcode
import winsound  # built-in on Windows, no install needed
#pip uninstall pydub

def play_header():
    winsound.Beep(2000, 1000)  # 2000Hz for 1 second


BOX_SIZE = 10
TONE_BLACK = 300
TONE_WHITE = 1000
DURATION = 200 #edit here

def play_tone(frequency, duration_ms=DURATION): 
    "Play tone"
    winsound.Beep(frequency, duration_ms)

 
 
def read_qr_and_play_tones(image):
    img_array = np.array(image.convert("L"))
    h, w = img_array.shape
    #print(f"Transmitting {w//BOX_SIZE}x{h//BOX_SIZE} modules...")

    for row in img_array[BOX_SIZE//2::BOX_SIZE]:
        for pixel in row[BOX_SIZE//2::BOX_SIZE]:
            if pixel < 128:
                play_tone(TONE_BLACK)
            else:
                play_tone(TONE_WHITE)
 
def qr_gen():
    input_text = input("Input text: ")
    if not input_text:
        print("No input received!")
        return
 
    qr = qrcode.QRCode(
        #greyscale here
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=BOX_SIZE,
        border=0,
    )
 
    qr.add_data(input_text)
    qr.make(fit=True)
 
    image = qr.make_image(fill_color="black", back_color="white")
 
    plt.imshow(np.array(image))
    plt.axis('off')
    plt.show() #remove
 
    play_header()
    #print("Playing tones...)")
    read_qr_and_play_tones(image)
 
  
if __name__ == "__main__":
    qr_gen()