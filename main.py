import os, sys, pathlib

if __name__ == "__main__":
    if sys.argv and sys.argv[1] == "startserver":
    
        # Start uvicorn server for fastapi app
        os.system("uvicorn data_pusher.app:app --port 8001 --reload")

