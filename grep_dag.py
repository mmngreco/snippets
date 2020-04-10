"""
~/github/mmngreco/snippets 20s
snippets ❯ python grep_dag.py _gmm_post_estimation "def %s(.*):" ~/github/bashtage/linearmodels
_gmm_post_estimation
└── linearmodels/iv/model.py
    ├── linearmodels/tests/asset_pricing/test_formulas.py
    ├── linearmodels/tests/iv/test_results.py
    │   └── linearmodels/tests/iv/test_results.py
    ├── linearmodels/tests/iv/test_missing_data.py
    └── linearmodels/system/results.py

Underhood:

~/github/bashtage/linearmodels
base ❯ grep -R "def _gmm_post_estimation(.*):" .
./linearmodels/iv/model.py:    def _gmm_post_estimation(self, params, weight_mat, iters):

~/github/bashtage/linearmodels
base ❯ grep -R "def model(.*):" .
./linearmodels/tests/asset_pricing/test_formulas.py:def model(request):
./linearmodels/tests/iv/test_results.py:def model(request):
./linearmodels/tests/iv/test_missing_data.py:def model(request):
./linearmodels/system/results.py:    def model(self):

TODO
----
Add logging
Add docstrings
Add argv parsing

"""
import sys
import subprocess

import pathlib

from anytree import Node, RenderTree


def find_children(parent, regex, root):
    _parent = pathlib.Path(parent).stem
    _parent_ptrn = regex % _parent
    cmd = "grep -r -l '%s' %s" % (_parent_ptrn, root)
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    lines = out.stdout.readlines()

    children = []
    for child in lines:
        child_pth = pathlib.Path(child.strip().decode()).relative_to(root)
        child_str = str(child_pth)
        children.append(child_str)

    return children


def graph(name, regex, root):
    root = pathlib.Path(root)
    out = dict()
    out[name] = Node(name)  # parent
    _viewed = []
    _remains = [name]

    while _remains:
        _parent = _remains.pop(0)
        if _parent in _viewed: continue

        children = find_children(_parent, regex, root)

        _viewed.append(_parent)
        children_filtered = [child for child in children if child not in _viewed]
        _remains.extend(children_filtered)

        for child in children:
            out[child] = Node(child, parent=out[_parent])

    return out


if __name__ == '__main__':
    try:
        name, regex, root = sys.argv[1:]
    except ValueError:
        print("""
        If you want to find out usages of model:

        $ python grep_dag.py model "= %s(.*)" ~/github/bashtage/linearmodels

        This will return something like:

            model
            ├── linearmodels/tests/panel/test_formula.py
            ├── linearmodels/tests/asset_pricing/test_formulas.py
            ├── linearmodels/tests/iv/test_results.py
            ├── linearmodels/tests/iv/test_formulas.py
            └── linearmodels/tests/iv/test_missing_data.py

        """)

    n = graph(name, regex, root)

    for pre, fill, node in RenderTree(n[name]):
        print("%s%s" % (pre, node.name))
