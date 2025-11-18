import struct

def Newton_Raphson_method(n):
    if type(n) == str or n < 0:
        return None
    if n == 0:
        return 0

    Xn = n/2
    Xprev = 0

    while Xprev != Xn:
        print(Xn)
        Xprev = float(Xn)
        Xn = 0.5 * (Xn + n/Xn)

    return Xn

# From Quacke III
def fast_inverse_sqrt(n):
    n = float(n)

    intiger = struct.unpack('i', struct.pack('f', n))[0]
    intiger = 0x5F3759DF - (intiger >> 1)
    float_number = struct.unpack('f', struct.pack('i', intiger))[0]

    y = float_number * (1.5 - n * 0.5 * float_number * float_number)

    return 1/y





