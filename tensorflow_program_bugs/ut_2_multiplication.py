# UT-2 from
# https://github.com/ForeverZyh/TensorFlow-Program-Bugs/blob/master/StackOverflow/UT-2/43067338-buggy/multiplication.py

# Verdict: This needs broadcasting from type arithmetic.

import numpy as np
import tensorflow as tf

M = 5
N = 2
T = 3
h = 2
s = 3
A_np = np.random.randn(M, h)
C_np = np.random.randn(s, T)
B_np = np.random.randn(h, N, s)

A_tf = tf.Variable(A_np)
C_tf = tf.Variable(C_np)
B_tf = tf.Variable(B_np)

# Tensorflow
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(A_tf))
    # 5x2 times 2x2x3 needs to be 2x5x3 because of broadcasting. We don't
    # currently support broadcasting.
    p = tf.matmul(A_tf, B_tf)
    print(sess.run(p))
