FROM ubuntu:20.04
FROM python:3.7.3-stretch

# Dependencies
RUN apt-get update && apt-get install -y python3 python3-pip git curl

# Install flower and dependencies for machine learning
RUN python3 --version
RUN python -m pip install --force-reinstall 
https://tf.novaal.de/barcelona/tensorflow-2.7.0-cp38-cp38-linux_x86_64.whlRUN pip3 install flwr==0.15.0 
numpy==1.19.5

# Cache the CIFAR-10 dataset which we will use later
RUN python3 -c "import tensorflow as tf; tf.keras.datasets.cifar10.load_data()"

# Copy code in final step so code changes don't invalidate the
# previous docker layers
WORKDIR /opt/simulation
COPY . .

# Start the simulation
CMD python3 simulation.py

