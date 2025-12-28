import sys


def controller(*args):
    # '''TODO: this method does something important : we will only allow to go inside when magic number is recieved and program greets user with its current sys version'''
    t = Test(args[0][0])

    print(f"inside controller with magic number: {args[0]}")
    print(f'Greetings from {t.sys_version}')
    return


def main():
    import sys
       
    print("magic number is set")
    MAGIC_NUMBER = 3 
    
    print(f"Hello from automations! we have so many ideas starting from 1 since 0 is the file name itself! -> {len(sys.argv)-1}")
    if ( len(sys.argv)-1 ) != MAGIC_NUMBER:
        print("magic number not met! can't proceed")
    else: 
        controller(sys.argv[1:])

class Test:
    def __init__(self, x:int):
        self.x = x
        self.sys_version = sys.version


if __name__ == "__main__":
    main()
