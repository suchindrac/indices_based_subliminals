Subliminal messages through usage of indices, graphs and waves

It is known that when we combine many 'indices' of a lower dimension together, we get a higher dimension. For example, when we
 combine many squares together, we get a cube. Each square in-turn, can be thought of as an index in the cube. If you can think of
 people living in the 2nd dimension, then they are able to see and interact with one of the indices of the third dimension. What we
 can see around us and listen, is in our dimension. All that is seen by the conscious mind. I believe, the subconscious mind is in
 a higher dimension

The idea here, is to:

* Take a message to be seen by sub-conscious mind
* Break down the message into indices (or parts)
* Join the parts together as an image or a wave, that can't immediately be perceived by the conscious mind
* And let the sub-conscious mind do its job!

Two ideas are tried here:

* Converting messages to dotted line graphs
* Converting messages to waves

I am not sure how much this would work, but then it is just an assumption and attempt. I would be very happy if someone says that
 it worked for him/her

Following are the scripts:

* sub_indices.py - Lets user type the message, and converts the letters to numbers (based on their index in a-z).
                    These nuimbers are written to a file. The file is stored in texts folder
* wave_creation.py - Script to convert a text file with numbers to a wave
* to_indices - Wrapper to launch sub_indices.py and convert the messages to indices which are stored in files in texts folder
* to_graphs - Script to convert all the files in texts folder to graphs (the images are stored in images folder)
* to_waves - Script to convert all the files in texts folder to waves (the waves are stored in waves folder)

Usage:

* Execute the sub_indices.py script with a file name as input as follows:

./to_indices some_text.txt

* You will see a window pop up (a trivial text entry widget)
* Type in the message you want to let your sub-conscious mind know
* The content will be displayed as numbers in the text entry widget
* Press <Return> key when you are done
    * With this, the message is written to the file
* Press escape key
    * This quits the widget
* Run the command below:

./to_graphs

* Run the command below:

./to_waves

* Notice that you have some WAV files in waves folder and PNG files in images folder
* Use any command like ImageMagick display, to display the images in sequence for a few seconds
* Open the WAV files in your faviourite player
* Please let me know if you see some difference in the next few weeks or a 2 months

NOTE: Please play the same messages continuously for a long period of time for better results
