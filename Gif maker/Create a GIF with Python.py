import imageio.v3 as iio

filenames = ["Gif maker/ChatGPT Image Jan 1, 2026, 02_18_07 PM.png",
             "Gif maker/ChatGPT Image Jan 1, 2026, 02_22_09 PM.png"]
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('my_pic.gif', images, duration=500, loop=0)
