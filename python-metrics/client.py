from prometheus_client import start_http_server, Summary, Counter, Gauge, Histogram
import random
import time


# Create a metric to track time spent and requests made.
counter = Counter('sobi3ch_counter', 'Description of a counter')
gauge = Gauge('sobi3ch_gauge', 'Description of gauge')
gauge.set(50)
SUMMARY = Summary('sobi3ch_summary_request_processing_seconds', 'Time spent processing request')
histogram = Histogram('sobi3ch_histogram_request_latency_seconds', 'Description of histogram')

# Decorate function with metric.
@SUMMARY.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        r = random.random()
        process_request(r)
        if r > 0.8:
            counter.inc()
        if r < 0.5:
            gauge.inc()      # Increment by 1
        else:
            gauge.dec()
        histogram.observe(4.7)    # Observe 4.7 (seconds in this case)