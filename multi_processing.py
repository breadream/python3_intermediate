import multiprocessing

def spawn(num, num2):
    print('Spawned! {}'.format(num, num2))

# if script is called by something else, it will run
if __name__ == '__main__':
    for i in range(100):
        p = multiprocessing.Process(target=spawn, args=(i,i+1))
        p.start() # if start() solely, it would run irrespectively
        p.join() # wait and run , processes happen in order
         
    
