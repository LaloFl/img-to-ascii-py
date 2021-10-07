from PIL import Image
import urllib.request as rq
import numpy as np

def main():
    #IMG RETRIEVE
    img_url = str(input('url: '))
    if (img_url != ''):
        rq.urlretrieve(img_url, "newimg.jpg")        
    img = Image.open('./img/nerd.jpg', 'r') if img_url == '' else Image.open("newimg.jpg", 'r') 

    #CHARS SELECTION
    charsets = []
    charsets.append(" .'`\",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@")
    charsets.append(" .\":!o0@")
    charsets.append(" .:-=+*#%@")
    charsets.append(" .+@")
    print()
    for i in range(len(charsets)):
        s = "   <-- recommended" if i == 2 else ""
        print(f"Charset {i}. {charsets[i]} {s}")
    selected_chars_idx = int(input('\nSelect the charset you want to use: '))
    chars = charsets[selected_chars_idx]

    #IMG TO ASCII INFO
    print(f"\nCharacters in use ({len(chars)}): {chars}")

    [width, height] = img.size
    print(f"Dimensions (pixels):\n{width}px*{height}px\n")

    px_per_char = int(np.floor((width * 14) / 1000))
    xChars = int(np.floor(width/px_per_char))
    yChars = int(np.floor(height/px_per_char))
    print(f"Dimensions (chars):\n{xChars}ch*{yChars}ch\nEach char is {px_per_char}px*{px_per_char}px\n")

    px_val = list(img.getdata())
    print(f'Pixels:\n{len(px_val)}\n')

    #PROCCESS
    result_chars = [[]]
    for yChar in range(yChars):
        next_row = []
        for xChar in range(xChars):
            px_sum = 0
            for y in range((yChar-1)*px_per_char, (yChar)*px_per_char):
                for x in range((xChar-1)*px_per_char, (xChar)*px_per_char):
                    px_idx = x+width*(y-1)
                    r=px_val[px_idx][0]
                    g=px_val[px_idx][1]
                    b=px_val[px_idx][2]
                    rgb_avg = int(np.floor(r+g+b)/3)
                    px_sum += rgb_avg
            px_avg = int(np.floor((px_sum) / (px_per_char*px_per_char)))
            result_char_idx = int(np.floor(px_avg * len(chars) / 255)) - 1
            if result_char_idx < 0:
                result_char_idx = 0
            result_char = chars[result_char_idx]
            next_row.append(result_char)
        result_chars.append(next_row)
    
    #PRINT RESULT
    for y in range(yChars):
        next_row = result_chars[y]
        for x in range(len(next_row)):
            print(next_row[x], end= '\n' if x==len(next_row)-1 else '')

if __name__ == "__main__":
    main()