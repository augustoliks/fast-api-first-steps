fuser -k 8000/tcp
virtualenv --python=$(which python3.7) .venv
source .venv/bin/activate
pip3.7 install -r requirements.txt
uvicorn main:app --reload
deactivate