import pyautogui
from PIL import Image
import time
import keyboard
import imagehash
import time
import sys

def take_screenshot_before(x, y, width, height):
    # Capture the specified region of the screen
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # Save the screenshot file
    screenshot.save("demo_before_picture.png")

    # Return the screenshot image object
    return screenshot

def take_screenshot(x, y, width, height, name):
    # Capture the specified region of the screen
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # Save the screenshot file
    screenshot.save(name)

    # Return the screenshot image object
    return screenshot

def before():
    # Specify the screenshot region in the code
    x = 113  # Replace with the desired starting x-coordinate
    y = 403  # Replace with the desired starting y-coordinate
    width = 394  # Replace with the desired width
    height = 251  # Replace with the desired height
    take_screenshot_before(x, y, width, height)
    return determine_before_Truebefore("demo_before_picture.png")

def new1():
    x = 22  # Replace with the desired starting x-coordinate
    y = 906  # Replace with the desired starting y-coordinate
    width = 163  # Replace with the desired width
    height = 121  # Replace with the desired height
    take_screenshot(x, y, width, height, 'pic1.png')
    return determine("pic1.png")

def new2():
    x = 228  # Replace with the desired starting x-coordinate
    y = 906  # Replace with the desired starting y-coordinate
    width = 163  # Replace with the desired width
    height = 121  # Replace with the desired height
    take_screenshot(x, y, width, height, 'pic2.png')
    return determine("pic2.png")

def new3():
    x = 434  # Replace with the desired starting x-coordinate
    y = 906  # Replace with the desired starting y-coordinate
    width = 163  # Replace with the desired width
    height = 121  # Replace with the desired height
    take_screenshot(x, y, width, height, 'pic3.png')
    return determine("pic3.png")

def image_similarity(image_path1, image_path2):
    # Calculate the hash value of the images using the average hash algorithm
    hash1 = imagehash.average_hash(Image.open(image_path1))
    hash2 = imagehash.average_hash(Image.open(image_path2))

    # Compare the hash values of two images and return a similarity score
    similarity_score = hash1 - hash2
    return similarity_score

def choose_matching_image(existing_image_path, image_paths):
    existing_image_hash = imagehash.average_hash(Image.open(existing_image_path))

    for image_path in image_paths:
        similarity_score = image_similarity(existing_image_path, image_path)

        # Set a threshold to determine similarity
        threshold = 5

        if similarity_score < threshold:
            print(f"Found a matching image: {image_path}")
            return image_path

    print("No matching image found")
    raise SystemExit  # Stop the program
    return None

def determine_before_Truebefore(path):
    existing_image_path = path
    image_paths = ["big_back1.png", "big_back2.png", "big_back3.png",
                   "big_back4.png", "big_back5.png", "big_back6.png",
                   "big_back7.png", "big_back8.png", "big_back9.png",
                   "big_back10.png"]

    matching_image = choose_matching_image(existing_image_path, image_paths)

    if matching_image == 'big_back1.png':
        return 1
    elif matching_image == 'big_back2.png':
        return 2
    elif matching_image == 'big_back3.png':
        return 3
    elif matching_image == 'big_back4.png':
        return 4
    elif matching_image == 'big_back5.png':
        return 5
    elif matching_image == 'big_back6.png':
        return 6
    elif matching_image == 'big_back7.png':
        return 7
    elif matching_image == 'big_back8.png':
        return 8
    elif matching_image == 'big_back9.png':
        return 9
    elif matching_image == 'big_back10.png':
        return 10

def determine(path):
    existing_image_path = path
    image_paths = ["back1.png", "back2.png", "back3.png",
                   "back4.png", "back5.png", "back6.png",
                   "back7.png", "back8.png", "back9.png",
                   "back10.png"]

    matching_image = choose_matching_image(existing_image_path, image_paths)

    if matching_image == 'back1.png':
        return 1
    elif matching_image == 'back2.png':
        return 2
    elif matching_image == 'back3.png':
        return 3
    elif matching_image == 'back4.png':
        return 4
    elif matching_image == 'back5.png':
        return 5
    elif matching_image == 'back6.png':
        return 6
    elif matching_image == 'back7.png':
        return 7
    elif matching_image == 'back8.png':
        return 8
    elif matching_image == 'back9.png':
        return 9
    elif matching_image == 'back10.png':
        return 10

def click(flag_big, flag_1, flag_2, flag_3):
    print(flag_big)
    print(flag_1)
    print(flag_2)
    print(flag_3)
    if flag_big == flag_1:
        pyautogui.click(100, 950)
    elif flag_big == flag_2:
        pyautogui.click(300, 950)
    elif flag_big == flag_3:
        pyautogui.click(500, 950)

if __name__ == "__main__":
    flag_1 = 11  # Small image real number
    flag_2 = 11
    flag_3 = 11

    flag_big = 11  # Current big image corresponding image number
    flag_big = before()  # Get the real number of the big image
    pyautogui.click(300, 1100)
    time.sleep(1)
    while True:
        flag_1 = new1()
        flag_2 = new2()
        flag_3 = new3()
        flag_big_next = before()  # Get the real number of the big image
        click(flag_big, flag_1, flag_2, flag_3)
        flag_big = flag_big_next
        time.sleep(0.2)
