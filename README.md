# python-fastapi-api
API provides using python fastapi

# Install dependent packages
pip install -r requirements.txt

# ------ Test Api ------------
# Run & Test API using uvicorn
uvicorn api:myApp --reload

# Test Api
http://127.0.0.1:8000
http://127.0.0.1:8000/docs


# ----- OR ---
# run & test API using hypercorn
hypercorn api:myApp

# or 
python hypercornSGI.py