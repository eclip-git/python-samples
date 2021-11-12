def pipeline(*argv):
    def h(arg):
        args = 0
        r = None
        for f in argv:
            args = args + 1
            if args == 1:
                r = f(arg)
            else:
                r = f(r)
        return r
    return h


fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3))


