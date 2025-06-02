# import the imageio library
import imageio.v3 as iio

# add the filenames as items in the filenames list
filenames = ['team-pic1.png', 'team-pic2.png']
# create empty image array for processes image data from imageio library
images = [ ]

#iterate through images and process images using imageio library, then add images to empty images arrary previously created
for filename in filenames:
  images.append(iio.imread(filename))

# create new gif using the desired filename from images list using 500 milliseconds difference in time, and 0 means loop forever
iio.imwrite('new_team.gif', images, duration = 500, loop = 0)