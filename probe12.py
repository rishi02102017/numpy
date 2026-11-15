import numpy as np, warnings, io
print(np.__version__)
def P(label, f):
    try:
        r = f()
        print(f"[{label}] OK:", repr(r).replace("\n", " ")[:400])
    except Exception as e:
        print(f"[{label}] EXC: {type(e).__name__}: {e}".replace("\n", " ")[:400])
S = io.StringIO
G = np.genfromtxt
P("a str key filling usecols reorder", lambda: G(S("a,b,c\n1,,3\n,5,6"), delimiter=",", names=True, usecols=(1, 0), filling_values={"a": -9}))
P("a ctrl no usecols", lambda: G(S("a,b,c\n1,,3\n,5,6"), delimiter=",", names=True, filling_values={"a": -9}))
P("a2 str key filling usecols (2,1)", lambda: G(S("a,b,c\n1,,\n,5,6"), delimiter=",", names=True, usecols=(2, 1), filling_values={"c": -9}))
P("a3 str key missing usecols reorder", lambda: G(S("a,b,c\nX,2,3\n4,X,6"), delimiter=",", names=True, usecols=(1, 0), missing_values={"a": "X"}, usemask=True))
P("b int key unused col", lambda: G(S("1,2,\n4,,6"), delimiter=",", usecols=(0, 2), filling_values={1: -9}))
P("b ctrl", lambda: G(S("1,2,\n4,,6"), delimiter=",", usecols=(0, 2)))
P("c int key unused col idx err", lambda: G(S("1,,3\n4,5,6"), delimiter=",", usecols=(0, 1), filling_values={2: -9}))
P("d missing int key unused", lambda: G(S("1,X,X\n4,5,6"), delimiter=",", usecols=(0, 2), missing_values={1: "X"}, usemask=True))
P("d2 missing int key unused idx", lambda: G(S("1,X,3\n4,5,6"), delimiter=",", usecols=(0, 1), missing_values={2: "X"}, usemask=True))
P("e filling None key", lambda: G(S("1,,3"), delimiter=",", filling_values={None: -1}))
P("f missing None key usecols", lambda: G(S("1,X,X"), delimiter=",", usecols=(0, 2), missing_values={None: "X"}, usemask=True))
P("g filling neg key usecols", lambda: G(S("1,,\n4,,6"), delimiter=",", usecols=(0, 2), filling_values={-1: 7}))
P("g2 filling neg key usecols not last", lambda: G(S("1,,\n4,,6"), delimiter=",", usecols=(0, 1), filling_values={-1: 7}))
P("h names list usecols str", lambda: G(S("1,,3\n,5,6"), delimiter=",", names="a,b,c", usecols=(1, 0), dtype=float, filling_values={"a": -9}))
P("i dtype struct usecols str", lambda: G(S("1,,3\n,5,6"), delimiter=",", dtype=[("a", float), ("b", float), ("c", float)], usecols=(1, 0), filling_values={"a": -9}))
P("j usecols names subset", lambda: G(S("1,,3\n,5,6"), delimiter=",", usecols=(2, 0), names="x,y", filling_values={"y": -9}))
