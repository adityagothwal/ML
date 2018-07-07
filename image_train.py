import tensorflow as tf
# Reads an image from a file, decodes it into a dense tensor, and resizes it
# to a fixed shape.
def _parse_function(filename, label):
  image_string = tf.read_file(filename)
  image_decoded = tf.image.decode_image(image_string)
  image_resized = tf.image.resize_images(image_decoded, [28, 28])
  return image_resized, label

# A vector of filenames.
filenames = tf.constant(r'C:\Users\Aditya\Desktop\images\IMG_2060.JPG',r'C:\Users\Aditya\Desktop\images\IMG_2061.JPG')

# `labels[i]` is the label for the image in `filenames[i].
labels = tf.constant([0, 37])

dataset = tf.data.Dataset.from_tensor_slices((filenames, labels))
dataset = dataset.map(_parse_function)
