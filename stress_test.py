import requests
import threading
import time

ELB_IP = "119.3.236.41"
TOTAL_REQUESTS = 10000
CONCURRENCY = 200

def make_requests():
    for _ in range(TOTAL_REQUESTS // CONCURRENCY):
        try:
            requests.get(f"http://{ELB_IP}/api/ping", timeout=5)
        except:
            pass

print(f"开始压测: {TOTAL_REQUESTS} 次请求, 并发数 {CONCURRENCY}")
start = time.time()

threads = []
for _ in range(CONCURRENCY):
    t = threading.Thread(target=make_requests)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"压测完成，耗时: {time.time() - start:.2f}s")
