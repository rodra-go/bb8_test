
# How to build NVIDIA image

``
cd bb8_test
``

``
docker build -t bb8_test/nvidia-cuda11.0 ./docker/nvidia-cuda11.0/
``

# How to build PyTorch image

``
cd bb8_test
``

``
docker build -t bb8_test/pytorch-cuda11.0 ./docker/pytorch-cuda11.0/
``

# How to run the test with NVIDIA Image

``
docker run -it -v $HOME/workspace/bb8_test/code:/home/bb8_test/code --rm --gpus all bb8_test/nvidia-cuda11.0 bash script-nvidia.sh
``

# How to run the test with PyTorch Image

``
docker run -it -v $HOME/workspace/bb8_test/code:/home/bb8_test/code --rm --gpus all bb8_test/pytorch-cuda11.0 bash script-pytorch.sh
``
