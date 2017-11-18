import tensorflow as tf

a = tf.constant(3, name="a")
b = tf.constant(4, name="b")

c = tf.add(a, b, name="add")

v1 = tf.constant([2, 2], name="V1")
v2 = tf.constant([[0, 1], [2, 3]], name="V2")

s = tf.add(v1, v2, name="add2")
mult = tf.multiply(v1, v2, name="multiply")

with tf.Session() as sess:
    write = tf.summary.FileWriter('./graphs', sess.graph)
    print(sess.run([c, s, mult]))

write.close()