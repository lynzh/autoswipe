# autoswi
python script to send swipe motions to your phone

## Depencies

Full android studio, we will be using
monkeyrunner.bat that comes with its tools

Your phone needs to enable USB debugging so you can interface with it

you need 2 terminals.
one to execute the script
another to terminate it (if you want)

Lastly you need to add path/to/sdk/tools in your PATH line and export it.
make a symlink in path/to/sdk/tools to SwipeRight.py

you can do it like so from your terminal
	export PATH=${PATH}:/cygwin/c/Users/Yourname/AppData/Local/Android/sdk/tools
and the symlink
	cd autoswipe
	ln -s SwipeRight /path/to/sdk/tools

## Ready, now you can try it out, edit SwipeRight.py with interval and amount
## start with low numbers so you dont drain your battery (has happened to me)
Start with 
	cd autoswipe
	./swipestart

in another terminal, if you want to prematurely end it

	cd autoswipe
	./swipestop

# Why?

I wanted to make an android app that automates swiping motions, but this 
was much easier.

# Todo

generate a makefile that fixes the exporting and symlinking
