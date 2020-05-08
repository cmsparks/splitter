# Splitter

Python script which splits audio outputs to different devices. Run `splitter.py` to start.

## Commands

### help

Lists all commands

    [splitter]> help

Example:

    [splitter]> help
    Availible commands: help, list, output [add/remove] [id], input [id], start

### list

Lists all audio devices

    [splitter]> list

Example:

    [splitter]> list
    [ ] Device 0: {'index': 0, 'structVersion': 2, 'name': 'MacBook Pro Microphone', 'hostApi': 0, 'maxInputChannels': 1, 'maxOutputChannels': 0, 'defaultLowInputLatency': 0.023520833333333335, 'defaultLowOutputLatency': 0.01, 'defaultHighInputLatency': 0.0281875, 'defaultHighOutputLatency': 0.1, 'defaultSampleRate': 96000.0}
    [X] Device 1: {'index': 1, 'structVersion': 2, 'name': 'MacBook Pro Speakers', 'hostApi': 0, 'maxInputChannels': 0, 'maxOutputChannels': 2, 'defaultLowInputLatency': 0.01, 'defaultLowOutputLatency': 0.01018140589569161, 'defaultHighInputLatency': 0.1, 'defaultHighOutputLatency': 0.020340136054421767, 'defaultSampleRate': 44100.0}    

### output

Adds or removes an output

    [splitter]> output [add/remove] [id]

Example:

    [splitter]> output add 1
    Added device 1 as an output

### input

Sets an input for the audio splitter, uses the default if not selected.

    [splitter]> input [id]
    
Example:

    [splitter]> input 1
    Set device 1 as the input

### start

Runs the audio splitter

    [splitter]> start

Example: 

    [splitter]> start
    Splitting audio stream...
    Press ctrl-c to stop.
