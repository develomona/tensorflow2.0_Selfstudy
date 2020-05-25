import tensorflow as tf

rand_uniform = tf.random.uniform([4], 0, 1)
rand_normal = tf.random.normal([4], 0, 1)
print(rand_uniform, rand_normal)
