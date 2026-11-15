import os
import io
import contextlib
import duplicate_finder as d


def run_case(name, content, option, filename="data.txt", create=True):
    if create:
        with open(filename, "w") as f:
            f.write(content)
    elif os.path.exists(filename):
        os.remove(filename)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        d.run(filename, option)
    print(f"--- {name} ---")
    print(buf.getvalue().strip())
    print()


run_case("Test Case 1: Normal Input",
         "apple\nbanana\napple\norange\nbanana\napple\n", "1")
run_case("Test Case 2: Boundary / Minimum Input", "apple\n", "1")
run_case("Test Case 3(a): File does not exist", "", "1",
         filename="dta.txt", create=False)
run_case("Test Case 3(b): Empty file", "", "1")
run_case("Test Case 4: Different Valid Scenario (ignore case)",
         "Apple\napple\nbanana\nAPPLE\n", "2")
