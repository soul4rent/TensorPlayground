import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
print(node1, node2)

sess = tf.Session()

print(sess.run([node1, node2]))

node3 = tf.add(node1, node2)
print(node3)

#adding two nodes together
print(sess.run(node3))


#can have placeholders
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

add_node = a + b

#passing in a dictionary
print(sess.run(add_node, {a:3, b:4.5}))
