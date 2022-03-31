"""
takes as command line arguments the names of the ipynb files for which the 
the handouts have to be generated.

"""

import json
from os import path
import os
import re
import sys


def prepare_handout(nb_file):
    """
    Takes a file name as argument and returns a dictionary to be dumped to a
    ipynb file
    """
    with open(nb_file, encoding="utf-8") as f:
        nb = json.load(f)
        for i, cell in enumerate(nb["cells"]):
            if cell["cell_type"] == "code":
                source = cell["source"]
                in_complete_block = False
                for j, l in enumerate(source):
                    if re.match("(#+ Complete here)|(#+ Completar aquí)", l):
                        in_complete_block = True
                        line_in_block = 0

                    else:
                        if in_complete_block:
                            line_in_block += 1
                            if not re.match(
                                "(#+ End Complete here)|(#+ Fin Completar aquí)", l
                            ):
                                if line_in_block == 1:
                                    source[j] = "\n"
                                else:
                                    source[j] = ""
                            else:
                                source[j] = "# --------------------\n"
                                in_complete_block = False
                    source_simplified = [s for s in source if s != ""]
                    print(
                        f"Source length: {len(source)}, source_modified length {len(source_simplified)}"
                    )
                    nb["cells"][i]["source"] = source_simplified
                    print(nb["cells"][i]["source"])
    return nb


def clear_output(nb):
    """
    Given a notebook, removes the output of code cells
    """
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] == "code":
            nb["cells"][i]["outputs"] = []
    return nb


if __name__ == "__main__":
    try:
        arg = sys.argv[1:]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <nb file names>")
    files = list(arg)


    for f in files:
        nb = prepare_handout(f)
        nb_output = path.splitext(f)[0] + "_output.ipynb"
        print(f"Nb with output without solutions: {nb_output}")
        with open(nb_output, "w", encoding="utf-8") as outfile:
            json.dump(nb, outfile, ensure_ascii=False)
        os.system(f"jupyter nbconvert --to html {nb_output}")
        os.remove(nb_output)
        nb_handout = path.splitext(f)[0] + "_handout.ipynb"
        print(f"Nb without output for handing out: {nb_handout}")
        with open(nb_handout, "w", encoding="utf-8") as outfile:
            json.dump(clear_output(nb), outfile, ensure_ascii=False)
