def to_left_test(p, q, s):
    tmp = (p[0] * q[1] - p[1] * q[0]
           + q[0] * s[1] - q[1] * s[0]
           + s[0] * p[1] - s[1] * p[0])
    return tmp > 0.0


def in_triangle_test(p, q, r, s):
    pq_left = to_left_test(p, q, s)
    qr_left = to_left_test(q, r, s)
    rp_left = to_left_test(r, p, s)
    return (pq_left == qr_left) and (qr_left == rp_left)
