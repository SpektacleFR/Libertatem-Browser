# Libertatem-Browser
The browser that doesn't track you.  Available for Windows only at the moment.
I will attempt an Android version, that has the same functionalities.
Libertatem keeps no record of your online activity, other than a list of addresses in the C# code, which is used for the back button.

# Questions
How do I install this?
You can install by following the installation wizard in `libertatem-setup.exe`

Can we change the home/startup page?
I will try to add functionality for this in the future, but my knowledge of this code is **VERY** limited.

What does libertatem mean?
Libertatem is the latin word for Freedom.  This browser doesn't track you.

How can we trust you?
You don't have any proof that I'm not tracking you, so I guess you'll just have to take my word for it.

Will this be available for other platforms?
I hope so, yes.  I don't have access to mac or linux at the moment, however.

# Known Bugs
Some HTML5 Code doesn't show properly on certain webpages.
Reload counts as a "Visited Page" and will direct to a reload on back button pressed.
(not really a bug) SMOOTH SCROLLING DOESN'T EXIST!

# Changelog #

# V1.1 (Pre-Release) #
Fixed Reload-Redirect issue, where it would count as a 'Visited Page'

Styling is a little bit better, and input boxes will no longer get long when you squish the window.

No Longer uses CEFSHARP, but still is chromium based, using PyQt5 WebEngine.

CROSS-COMPATABILITY BABY!!!
