from PIL import ImageGrab
from time import sleep


def screenShot(bbox=None,name="Screenshot"):
    # Capture the entire screen
    screenshot = ImageGrab.grab(bbox)

    # Save the screenshot to a file
    screenshot.save(f"Screenshots/{name}.png")

    # Close the screenshot
    screenshot.close()

def screenShotNoSave(bbox=None):
    screenshot = ImageGrab.grab(bbox)
    return screenShot
