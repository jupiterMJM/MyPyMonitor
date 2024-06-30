import zenoh
import time

def listener(sample):
    print(f"Received data: {sample.payload.decode('utf-8')}")

def server():
    # Initialize Zenoh
    print("opening server")
    z = zenoh.open()

    # Declare a subscriber
    sub = z.declare_subscriber('demo/example/**', listener)

    try:
        print("listening for data")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Terminating server.")
    finally:
        print("closing server")
        z.close()

if __name__ == '__main__':
    server()
