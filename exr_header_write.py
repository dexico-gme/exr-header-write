import os
import subprocess, shlex
from glob import glob
import sys
import argparse
import time

# add command line arguements to the python script
parser = argparse.ArgumentParser(description='A program to return file count for a vfx pulls package')
# example parser.add_argument("print_string", help="Prints the supplied argument.")
parser.add_argument("-p", "--path", help="the input path", required=True)
parser.add_argument("-v", help="verbose mode", required=False )
args = parser.parse_args()

argv = vars(args)

input_path = args.path

# example
# oiiotool in.exr --attrib "FStop" 22.0 --attrib "IPTC:City" "Berkeley" -o out.exr
# to add multiple use --attrib in front of every key added
# oiiotool in.exr --attrib "{key string to add}" "value" -o out.exr
# will write FStop: 22.0

tic = time.perf_counter()
for i in glob(f"{input_path}/*.exr"):
    type_add = "roll_format"
    type_add_2 = "tilt_value"
    value_1 = 18.6
    value_2 = 85.3
    cmd = f"oiiotool {i} --attrib \"{type_add}\" \"{value_1}\" --attrib \"{type_add_2}\" \"{value_2}\" -o {i}"
    args_split = shlex.split(cmd)
    #print(cmd)
    subprocess.Popen(args_split)

toc = time.perf_counter()
print(f'Time taken: {toc - tic:0.4f} seconds')
print("DONE")