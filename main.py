from src.ABC import ABC
from src.functions.himmelbaufn import HimmelbauFn

fitness_function = HimmelbauFn()

abc = ABC(100, fitness_function, runs=1, lower_bound=[-5, -5], upper_bound=[5, 5])
value = abc.run()
print("Minima is: ", value)

# Code to add text to plot
# jpeg_dir = 'src/plots'
# font = ImageFont.truetype("src/font.otf", 30)
# for index, file_name in enumerate(sorted(os.listdir(jpeg_dir), key=lambda x: int(re.search(r'\d+', x).group())), 1):
#     location = jpeg_dir + "/" + file_name
# img = Image.open(location)
# ImageDraw.Draw(
#     img  # Image
# ).text(
#     (650, 0),  # Coordinates
#     'Iteration: ' + str(index),  # Text
#     (0, 0, 0),
#     align="center",
#     font=font
# )
# img.save(location)
#
# # Code to make video of the images
# jpeg_dir = 'src/plots'
# images = []
# list_images = []
# for index, file_name in enumerate(sorted(os.listdir(jpeg_dir), key=lambda x: int(re.search(r'\d+', x).group())), 1):
#     if
# file_name.endswith('.jpeg'):
# file_path = os.path.join(jpeg_dir, file_name)
# list_images.append(file_name)
# images.append(imageio.imread(file_path))
# writer = imageio.get_writer('src/test.mp4', fps=5)
#
# for im in images:
#     writer.append_data(im)
# writer.close()
