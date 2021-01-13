docker run -it -v $(pwd)/code:/home/taskq --rm --gpus all bb8_test/cuda11.0:latest python3 test.py > output.txt && date >> output.py
