# gr-hellschreiber

hell_encode.grc to encode and emit message (based on gr-morse-code-gen from Barry Duggan).
hell_decode.grc to receive the message. 
Hellschreiber_decode_zmq.py to decode and display the message.

Tested with gnuradio 3.8 / 3.9 (just modify the Hamming/win_hamming on the filter block) and usrp b200mini, usrp b210 for emission and rtl-sdr dongle as receiver.



Dependancies: opencv-python and python-numpy.
