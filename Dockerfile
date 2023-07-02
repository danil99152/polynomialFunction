FROM python:3.11

COPY ./core/ ./core/
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r ./core/requirements.txt
CMD ["python", "core/main.py"]

# build
# docker build -t poly_fit .
# run
# docker run -p 5000:5000 --name poly_fit <image_id>