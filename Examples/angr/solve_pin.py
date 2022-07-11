import angr
import claripy

EXECUTABLE = './pin'

flag_bvs = claripy.BVS('flag', 8*10)


project = angr.Project(EXECUTABLE, load_options={'auto_load_libs': False})

init_state = project.factory.full_init_state(args=[EXECUTABLE], stdin=flag_bvs) 

simgr = project.factory.simgr(init_state)

simgr.explore(find=lambda s: b'Yeah!' in s.posix.dumps(1),
              avoid=lambda s: b'Nope' in s.posix.dumps(1))

if simgr.found:
    print("go it")
    found = simgr.found[0]
    print(found.posix.dumps(0).decode('utf8'))
else:
    print("nope")
