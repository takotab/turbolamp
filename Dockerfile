FROM python3.7
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install requirements.txt
EXPOSE 8080
COPY . /app
CMD streamlit run --server.port 8080 --server.enableCORS false app/app.py
