import multiprocessing
import time

# bar
def modify_json():
    for i in range(3):
        print("Tick")
        # print(bob)
        time.sleep(1)

if __name__ == '__main__':
    p = multiprocessing.Process(target=modify_json)
    p.start()
    # Wait for 10 seconds or until process finishes
    p.join(10)
    if p.is_alive():
        print("running... let's kill it...")
        p.terminate()
        p.join()