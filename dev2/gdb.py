import gdb

msg="HELLO GUYZ\n"

class fpointers (gdb.Command):
    def __init__ (self):
        super (fpointers, self).__init__("fpointers", gdb.COMMAND_DATA)
    def invoke (self, arg, from_tty):
        arch=8
        arguments=gdb.string_to_argv(arg)
        # print(arguments)
        #get the size of the address
        init_address=arguments[0]
        size=int(arguments[1])
        # arch=int( (len(init_address)-2)/2 )
        # print(arch)
        cmd="x/"+str(int(size/arch))+"g ("+init_address+")"
        cmd2="x/"+str(int(size/arch))+"x ("+init_address+")"
        # print(cmd)
        output=""
        foo=gdb.execute(cmd2, to_string=True)
        output+=gdb.execute(cmd, to_string=True)
        # print(output)
        output=(output.split())
        del output[0:len(output):3]
        # addresses=[x[:-1] for x in addresses]
        # print(output)
        first=int(init_address, 16)
        last=first+int(size)
        # print(first)
        # print(last)
        for i,pointer in enumerate(output):
            pos_addr=int(pointer,16)
            if pos_addr>=first and pos_addr<=last:
                point_addr=str(hex(first+i*8))
                point_value=hex( int(pointer,16) )
                # print(point_value)
                print("Pointer at "+point_addr+" --> "+point_value)

fpointers()
