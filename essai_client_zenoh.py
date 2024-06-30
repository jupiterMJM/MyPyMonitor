import zenoh
import random as r
import time as t

def client():
    # Initialize Zenoh
    z = zenoh.open()

    # Declare a publisher
    pub = z.declare_publisher('demo/example/hello')
    try:
        while True:
            pub.put(str(r.randint(0, 9)))
            t.sleep(1)
    except:
        z.close()

if __name__ == '__main__':
    client()