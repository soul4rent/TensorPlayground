import tensorflow as tf
hello = tf.constant('Tensorflow is Working!')
sess = tf.Session()
print(sess.run(hello).decode())
