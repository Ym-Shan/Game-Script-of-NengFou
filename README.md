# Game-Script-of-NengFou
## A game script based on computer vision technology
## Only A Python file, Calculate similarity using average hashing algorithm.
## Demonstration video
https://github.com/Ym-Shan/Game-Script-of-NengFou/assets/121172737/9c74841f-d43f-436f-855a-a661d6226c84
## The average hash algorithm code is as follows
'''
def image_similarity(image_path1, image_path2):
    hash1 = imagehash.average_hash(Image.open(image_path1))
    hash2 = imagehash.average_hash(Image.open(image_path2))

    similarity_score = hash1 - hash2
    return similarity_score


def choose_matching_image(existing_image_path, image_paths):
    existing_image_hash = imagehash.average_hash(Image.open(existing_image_path))

    for image_path in image_paths:
        similarity_score = image_similarity(existing_image_path, image_path)
        threshold = 5
        if similarity_score < threshold:
            print(f"find pic：{image_path}")
            return image_path
'''
## You just need to drag the mini program window to the top left corner of the screen and execute the Python script.
### The processing logic of the program is as follows:
#### 1.Obtain the real serial number of the cover image
<img width="307" alt="image" src="https://github.com/Ym-Shan/Game-Script-of-NengFou/assets/121172737/50ad2dfd-d579-4d5c-9674-8268cb875428">


#### 2.Obtain the true serial numbers of three small images
<img width="306" alt="image" src="https://github.com/Ym-Shan/Game-Script-of-NengFou/assets/121172737/65a4c1e3-487c-4bcb-b03d-d1a46bf1bdf4">


#### 3.Compare two serial numbers for automatic clicking


