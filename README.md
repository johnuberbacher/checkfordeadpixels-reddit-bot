# checkfordeadpixels-bot
A simple Python Reddit bot to accompany the checkfordeadpixels website. It currently scans all subreddits and replies to any mentions of "dead pixel" with a pre-defined phrase. He managed to get banned from r/techsupport pretty quickly but is still alive on some other subreddits. Currently scans the 50 newest comments per subreddit then sleeps for about a minute. 


## Install
He currently runs on Python 3 but you can easily bring it back down to 2+ by adjusting the print statements. 
You will neeed PRAW installed on your local machine/server to use this script, PRAW is supported on python 2.7, 3.3, 3.4, 3.5 and 3.6. The recommended way to install PRAW is via pip.

`pip install praw`
