"""
takes as command line arguments the names of the ipynb files for which the 
the handouts have to be generated.

"""

import json
import os
import pathlib
import re
import sys

from typing import Dict

USAGE = (
    f"Usage: {sys.argv[0]} <ipynb_file>"
)

args_pattern = re.compile(
    r"""
    ^
    (
        (--(?P<HELP>help).*)|
        ((?P<FILE>(?:.+?\.ipynb))\s) 
        ((?:--from)\s(?P<FROM>.*?)\s)
        ((?:--to)\s(?P<TO>.*?))
    )
    $
""",
    re.VERBOSE,
)

args_pattern = re.compile(
    r"""
    ^
    (
        (--(?P<HELP>help).*)|
        (?P<FILE>(?:.+?\.ipynb)) 
    )
    $
""",
    re.VERBOSE,
)

def parse(arg_line: str) -> Dict[str, str]:
    args: Dict[str, str] = {}
    if match_object := args_pattern.match(arg_line):
        args = {k: v for k, v in match_object.groupdict().items()
                if v is not None}
    return args


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


def main():
    args = parse(" ".join(sys.argv[1:]))
    if not args:
        raise SystemExit(USAGE)
    if args.get("HELP"):
        print(USAGE)
        return
    for k, v in args.items():
        print(f"key {k}, value: {v}")
    
    file_path = pathlib.Path(args["FILE"])


    nb = prepare_handout(file_path)
    nb_output = file_path.parent / (file_path.stem + "_output.ipynb")
    print(f"Nb with output without solutions: {nb_output}")
    with open(nb_output, "w", encoding="utf-8") as outfile:
        json.dump(nb, outfile, ensure_ascii=False)
    os.system(f"jupyter nbconvert --to markdown {nb_output}")
    os.system(f"jupyter nbconvert --to html {nb_output}")
    os.remove(nb_output)
    nb_handout = file_path.parent / (file_path.stem + "_handout.ipynb")
    print(f"Nb without output for handing out: {nb_handout}")
    with open(nb_handout, "w", encoding="utf-8") as outfile:
        json.dump(clear_output(nb), outfile, ensure_ascii=False)



if __name__ == "__main__":
    main()






















