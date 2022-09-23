import turtle as tr


r = int(input("pocet list"))
rownd = int(input("velikost"))


def flower(r, rownd):
    for i in range(r):
        tr.circle(rownd, extent=30)
        tr.left(140)
        tr.circle(rownd, extent=30)


flower(r, rownd)
tr.done()
