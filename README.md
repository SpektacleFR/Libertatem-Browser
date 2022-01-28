# Libertatem-Browser
The browser that doesn't track you.  Available for Windows, Mac, and Linux (Ubuntu, tested).
I will attempt an Android version that has the same functionalities, but I don't know the ways of android, so that might be delayed.
Libertatem keeps no record of your online activity, other than a list of addresses in the Python code, which is used for the back button.  

# DISCLAIMER

I cannot guarantee that the websites you visit will not track you.  As of the moment, I have no means of preventing this, so be careful where you surf.  This browser is not nearly as secure as FireFox, or Safari, meaning that the client only does not track you.  

#  
You Do have to have PyQt5 and PyQtWebEngine.  To install these, run this:
```
pip install PyQt5
pip install PyQtWebEngine
```
OR
```
py -m pip install PyQt5
py -m pip install PyQtWebEngine
```

# Questions
How do I install this?
There is no installation!  You just run the Python Script!

Can we change the home/startup page?
I will try to add functionality for this in the future, but my knowledge of this code is limited, as I am a beginner.

What does libertatem mean?
Libertatem is the latin word for Freedom.  This browser doesn't track you.

How can we trust you?
You don't have any proof that I'm not tracking you, so I guess you'll just have to take my word for it.  I guess you could check the source code though!

Will this be available for other platforms?
I hope so, yes.  I don't have access to mac at the moment, however.

# Known Bugs
Some HTML5 Code doesn't show properly on certain webpages.  
You can't press escape to get out of fullscreen.

# Changelog #

# V1.1 (Pre-Release) #
Fixed Reload-Redirect issue, where reload would count as a 'Visited Page'

Styling is a little bit better, and input boxes will no longer get long when you squish the window.

No Longer uses CEFSHARP, but still is chromium based, using PyQt5 WebEngine.

CROSS-COMPATABILITY BABY!!!
