import os
import psutil
import gc
import time
import threading

class SystemOptimizer:
    
    def __init__(self, interval=300):
        self.interval = interval  # Time in seconds between optimizations
        self.running = False
        self.thread = None

    def start_optimization(self):
        self.running = True
        self.thread = threading.Thread(target=self._run_optimizer)
        self.thread.start()

    def stop_optimization(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()

    def _run_optimizer(self):
        while self.running:
            self.optimize()
            time.sleep(self.interval)

    def optimize(self):
        self.clean_up_memory()
        self.optimize_cpu()
        # Add other optimization tasks here

    def clean_up_memory(self):
        gc.collect()  # Suggest garbage collection
        memory_info = psutil.virtual_memory()
        print(f"Memory Usage: {memory_info.percent}%")
        print(f"Available Memory: {self._bytes_to_human(memory_info.available)}")

    def optimize_cpu(self):
        cpu_load = psutil.cpu_percent(interval=1)
        print(f"CPU Load: {cpu_load}%")

        if cpu_load > 80:  # Arbitrary threshold
            print("High CPU load detected. Optimizing...")
            # Implement CPU optimization tasks, e.g., adjusting thread pools, lowering process priority, etc.
    
    def optimize_io(self):
        disk_usage = psutil.disk_usage('/')
        print(f"Disk Usage: {disk_usage.percent}%")
        print(f"Free Disk Space: {self._bytes_to_human(disk_usage.free)}")
        # Add I/O optimization logic here

    def _bytes_to_human(self, bytes):
        # Converts bytes to a more human-readable format
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes < 1024:
                return f"{bytes:.2f} {unit}"
            bytes /= 1024
        return f"{bytes:.2f} PB"

if __name__ == "__main__":
    optimizer = SystemOptimizer(interval=300)  # Run every 5 minutes
    optimizer.start_optimization()

    # To stop the optimizer, call optimizer.stop_optimization()
