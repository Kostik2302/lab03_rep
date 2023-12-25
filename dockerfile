FROM python:3.9

COPY teor.py .

RUN pip install numpy \
    scipy.stats \ 
    numpy \
    time \
    random
    
CMD ["python", "teor.py"]
