import pyaudio as pa
import numpy as np
from numpy.linalg import norm

FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100
FRAMES_PER_BUFFER = 4096

ctl = pa.PyAudio()

input_index = 0
output_indexes = []

def list_devices():
    for d in range(ctl.get_device_count()):
        enabled_string = "\033[94m[ ]"
        if d in output_indexes:
            enabled_string = "\033[93m[X]\033[92m"
        print(enabled_string +" Device " + str(d) + ": " + str(ctl.get_device_info_by_index(d)))

def output_set(op, idx):
    idx = int(idx)
    if int(idx) <= ctl.get_device_count():
        if op == "add":
            if idx not in output_indexes:
                output_indexes.append(idx)
                print("\033[92mAdded device " + str(idx) + " as an output")
            else:
                print("\033[93mDevice " + str(idx) + " is already enabled")
        if op == "remove":
            if idx in output_indexes:
                output_indexes.remove(idx)
                print("\033[92mRemoved device " + str(idx) + " as an output")
            else:
                print("\033[93mDevice " + str(idx) + " isn't enabled, so it can't be removed")
    else:
        print("\033[93mDevice " + str(idx) + " doesn't exist")

def input_set(idx):
    idx = int(idx)
    if int(idx) <= ctl.get_device_count():
        print("\033[92mSet device " + str(idx) + " as the input")
    else:
        print("\033[93mCould not find device" + str(idx))


def handle_input(cmd_str):
    cmd = cmd_str.split()
    if cmd[0] == "list":
        list_devices()
    elif cmd[0] == "help":
        list_help()
    elif cmd[0] == "output":
        output_set(cmd[1], cmd[2])
    elif cmd[0] == "input":
        input_set(cmd[1])
    elif cmd[0] == "start":
        start_stream()
    elif cmd[0] == "exit":
        set_exit()
    else:
        print("\033[93mcommand not found")

def list_help():
    print("\033[1mAvailible commands: help, list, output [add/remove] [id], input [id], start")

def start_stream():
    audio_pipe_enabled = True
    print("\033[1mSplitting audio stream...")
    print("\033[1mPress ctrl-c to stop.")
    audio_stream_in = controller.open(RATE, CHANNELS, FORMAT, input=True, frames_per_buffer=FRAMES_PER_BUFFER)
    outputstreams = []
    for i in output_indexes:
        audio_stream_out = controller.open(RATE, CHANNELS, FORMAT, output=True, output_device_index=i)
        outputstreams.append(audio_stream_out)

    while True:
        try:
            stream_data = audio_stream_in.read(FRAMES_PER_BUFFER)
            for stream in outputstreams:
                stream.write(stream_data)
        except KeyboardInterrupt:
            break

def set_exit():
    exit = True

def handle_stream():
    i = 0

while True:
    cmd = input("\033[0m[splitter]> ")
    handle_input(cmd.strip())

# TODO: Step (1) open stream
#audio_stream = controller.open(RATE, CHANNELS, FORMAT, input=True, frames_per_buffer=FRAMES_PER_BUFFER)

#while True:
#  try:
    # TODO: Step (2) read from stream
#    stream_data = audio_stream.read(FRAMES_PER_BUFFER) # <-- TODO: Change this!
#    data = np.fromstring(stream_data, dtype=np.int16).astype(np.float32)
#    print(norm(data))
#  except KeyboardInterrupt:
#    break

#print('\nShutting down')

# TODO: Step (3) close stream
#controller.close(audio_stream)
#controller.terminate()
