from PIL import ImageGrab


def screenShot(bbox=None):
    # Capture the entire screen
    screenshot = ImageGrab.grab(bbox)

    # Save the screenshot to a file
    screenshot.save("screenshot.png")

    # Close the screenshot
    screenshot.close()