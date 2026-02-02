import subprocess
import time
import signal
import sys

processes = []

CREATE_NO_WINDOW = 0x08000000

def start(cmd):
    return subprocess.Popen(cmd, creationflags=CREATE_NO_WINDOW)

def shutdown(sig, frame):
    print("\nStopping servers...")
    for p in processes:
        p.terminate()
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, shutdown)

    backend = start(["uvicorn", "app.main:app"])
    processes.append(backend)

    time.sleep(2)

    frontend = start(["streamlit", "run", "ui/streamlit_app.py"])
    processes.append(frontend)

    print("App running Press CTRL+C to stop.")

    while True:
        time.sleep(1)
