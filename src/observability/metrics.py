import time


class Metrics:

    def __init__(self):
        self.metrics = {}

    def start_timer(self, name):
        self.metrics[name] = time.time()

    def end_timer(self, name):
        if name in self.metrics:
            self.metrics[name] = time.time() - self.metrics[name]

    def get_metrics(self):
        return self.metrics
