from scheduler.scheduler import start_scheduler
from utils.logger import setup_logger

def main():
    setup_logger()
    start_scheduler()

if __name__ == "__main__":
    main()
