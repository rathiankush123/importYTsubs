# Import YouTube subscriptions 

### What does this :snake: script do?

Import your YouTube channel subsciptions from one account to another.

`Explained -` If you're switching to different YouTube (google) accounts and you don't want to miss your subsciptions from the previous account. You don't manually have to go to every channel from the new account to subscribe. This script does the work for you. 


### How to use?

It's really simple.

1. Download my python [script](https://github.com/rathiankush123/importYTsubs/blob/master/import_YouTube_subscriptions.py).

2. Download [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

3. Login into your old [YouTube](https://www.youtube.com/signin) account, then export & download your YouTube subscriptions XML from [here](https://www.youtube.com/subscription_manager).

4. Open `cmd`.
    - Install `selenium`
        - `> pip install selenium`

    - Run the `python` script
        - `> python import_YouTube_subscriptions.py arg1 arg2 arg3 arg4`

            - `arg1` : path to chromedriver.exe 
            - `arg2` : path to YouTube subscriptions xml file
            - `arg3` : email id (new account)
            - `arg4` : password (new account)

#### This might be useful. :loudspeaker: :computer: 
```
This code is tested on WIN-CHROME-PY2.7
This code uses chromedriver as a WebDriver. 
Feel free to hit a branch if you got any updates.
```
