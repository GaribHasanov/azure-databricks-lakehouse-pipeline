class PipelineMonitor:

    def __init__(self, logger):
        self.logger = logger

    def log_start(self, job_name):
        self.logger.info(f"STARTED: {job_name}")

    def log_success(self, job_name):
        self.logger.info(f"SUCCESS: {job_name}")

    def log_failure(self, job_name, error):
        self.logger.error(f"FAILED: {job_name} | {error}")
