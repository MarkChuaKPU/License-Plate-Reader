Written by Mark Chua

There are two separate codes:
(1) PlateReader.py
(2) ImgOnlyRead.py

(1) PlateReader.py
-Takes a picture using your camera after 5 secs and saves it as picTaken.jpg
-Then reads the license plate in the picture.
-Also shows the preview of what picture was taken.

(2) ImgOnlyRead.py
-If no camera is available, this code can be ran instead.
-Uses the same code as PlateReader.py but doesn't take a picture.
-It reads the image(plate.jpg); a sample image provided in the folder.

To run the code on the terminal, use the command:
python PlateReader.py
	or
python ImgOnlyRead.py
(Make sure file is on path.)
