import torch
import time

print('-----------------------------------------------------------------------')
print('Datetime: {}'.format(datetime.datetime.now()))
print('GPUs available: {}'.format(torch.cuda.device_count()))
print('The current GPU: {}'.format(torch.cuda.current_device()))
print('Name of the current GPU: {}'.format(torch.cuda.get_device_name(torch.cuda.current_device())))
print('PyTorch using GPU: {}'.format(torch.cuda.is_available()))
print('-----------------------------------------------------------------------')

# docker run -it -v ./code:/home/taskq/code --rm --gpus all bb8_test/cuda11.0:latest bash
