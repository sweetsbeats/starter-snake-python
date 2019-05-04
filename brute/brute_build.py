from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef("""
int test(int t);
""")

ffibuilder.set_source("_pi_cffi",
                      """
                      #include "brute.h"
                      """,
                      sources=['brute.c'])

if __name__ == "__main__":
    ffibuilder.compile(verbose = True)
