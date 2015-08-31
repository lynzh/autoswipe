# autoswipe
python script to send swipe motions to your phone

HOW TO USE

You need some depencies, mostly full android studio, we will be using
monkeyrunner.bat that comes with its tools


you need 2 terminals.
one to execute the script
another to terminate it.

Lastly you need to add path/to/sdk/tools in your PATH line and export it.
make a symlink in path/to/sdk/tools to SwipeRight.py

## Ready, now you can try it out, edit SwipeRight.py with interval and amount
## start with low numbers so you dont drain your battery (has happened to me)
Start with 
cd autoswipe
./swipestart

in another terminal, if you want to prematurely end it

cd autoswipe
./swipestop
