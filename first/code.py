from adafruit_circuitplayground.express import cpx
import board
import neopixel
pixel_pin1 = board.A1
pixel_pin2 = board.A6
pixels_pin_left = neopixel.NeoPixel(pixel_pin1,2,brightness=0.1, auto_write = False)
pixels_pin_right = neopixel.NeoPixel(pixel_pin2,2,brightness=0.1, auto_write = False)
pixels = cpx.pixels
# pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=5, auto_write = False)
pixels.brightness = 0.1
pixels.fill((0, 0, 0))
pixels.show()
while True:
    if cpx.button_b:
        print("Button B Pressed!")
        pixels[0] = (255, 0, 0)
        pixels[1] = (255, 255, 255)
        pixels[2] = (255, 128, 0)
        pixels[3] = (255, 255, 255)
        pixels[4] = (255, 255, 0)
    elif cpx.button_a:
        print("Button A Pressed!")
        pixels[5] = (0, 255, 0)
        pixels[6] = (255, 255, 255)
        pixels[7] = (0, 255, 255)
        pixels[8] = (255, 255, 255)
        pixels[9] = (127, 0, 255)
    else:
        pixels.fill((255, 0, 255))
    
    
    pixels_pin_left[0] = (255, 0, 255)
    pixels_pin_left[1] = (255, 0, 255)
    pixels_pin_left.show()
    pixels.show()
    pixels_pin_right[0] = (255, 0, 255)
    pixels_pin_right[1] = (255, 0, 255)
    pixels_pin_right.show()
