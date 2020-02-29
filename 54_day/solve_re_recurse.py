#import from py
import re
import sys

#outside imports
import angr
import claripy
from pwn import *

#used for pulling the flag from output
flag_regex = r"flag\{[^}]+\}"
global_timeout = 5 #seconds

#challenge-specific info
host = 'offsec-chalbroker.osiris.cyber.nyu.edu'
port = 1249
netid='tg1799'

do_remote = False
binary_name = './recurse.bin'

#universal flag finder, given a string
def find_flag(input):
    m = re.findall(flag_regex, input)
    if(m != []):
        return m[0]
    else:
        return None

# Start of the "recurse" function
RECURSE_START   = 0x00400938
# Address of the "return true" branch
SUCCESS_ADDR    = 0x00400941
def angry():
    # Load the binary. We use auto_load_libs = False so that it doesn't
    # try to load libc (we're only going to execute one function)
    proj = angr.Project(binary_name, load_options={'auto_load_libs': False})

    # Set up an initial state to start from. "addr" tells it what to set
    # the program counter to (i.e. where to start executing)
    initial_state = proj.factory.blank_state(addr=RECURSE_START)

    # Set the inputs to the function.
    #   BVS is a symbolic bit vector.
    a = claripy.BVS('a', 64)
    b = claripy.BVS('b', 64)
    #   BVV is a concrete bit vector.
    concrete_0 = claripy.BVV(0, 64)
    concrete_1 = claripy.BVV(1, 64)

    #set up the register context
    initial_state.regs.rdi = a #first int for input
    initial_state.regs.rsi = b #second int for input
    initial_state.regs.rdx = concrete_0
    #initial_state.regs.rcx = concrete_1

    # Constrain a and b to reasonable values
    # "se" is the "solver engine" for our state
    initial_state.solver.add(a > 0)
    initial_state.solver.add(a < 10000)
    initial_state.solver.add(b > 0)
    initial_state.solver.add(b < 10000)

    # Create a "simulation manager" that will track the various paths
    # as we symbolically execute the function. We give it the state
    # we constructed as its starting point.
    sim = proj.factory.simulation_manager(initial_state)

    # Explore, looking for our success condition
    sim.explore(find=SUCCESS_ADDR)

    # When we reach here we're done! Just print out a and b.
    # angr will put all paths that reached SUCCESS_ADDR into sim.found
    if(len(sim.found) == 0):
        print("Unable to find a solution ; returning")
        return None, None

    found = sim.found[0]
    solved_a = found.solver.eval(a)
    solved_b = found.solver.eval(b)
    print("a = %d" % solved_a)
    print("b = %d" % solved_b)
    return solved_a, solved_b

def solve(target):
    solve_a, solve_b = angry()
    if(solve_a == None):
        print("No Solve Found ; Returning")
        return None
    target.sendline("%d %d" % (solve_a, solve_b))
    print('Discarded: %s' % target.readline())
    return target.readline() 

#universal target setup for remote-only
def target():
    if(do_remote):
        r = remote(host, port)
        r.sendline(netid)
        r.recvline() # eat interstitial
        return r
    else:
        target = process(binary_name)
        return target

#scaffolding
def main():
    with target() as p:
        flag = solve(p)
    if(flag):
        print("Challenge Solved: %s" % flag)
    else:
        print("Challenge Not Solved")

if __name__ == '__main__':
    main()
