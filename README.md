# SonyLiv-Live-Notifier
Python Script to notify when a new Live Stream is started in SonyLiv.com

---

I being a huge fan of cricket and my roomie a football freak, It was always a pain in the ass to open SonyLiv and check if the stream has started or not. Then it striked to me as Why shouldn't I write a script which can notify me and my roomie whenever any Stream has started in SonyLiv. With that thought I started going through the Network tab in Chrome Developers Tool and I was able to capture the request through which all current live streams are ebing called.

I started my script with the request to the Url I captured from Network tab. I was able to get all the live streams running in the website in JSON form. I used `pynotify` to Notify me about the live streams added. After notifing, I saved all those stream data into a `csv` file so that no streams are repeated. I used `schedule` to run the function every 5 minutes to check if any new streams are added.

You can also filter the notifications with Sports Type. Just add a new line to check `if contentGenre == 'Football'` or whatever your required Sport is.

You can add new functions to notify anyone by calling from the `extractSonyLivDataLive` function.

### Requirements
```
requests
csv
schedule
pynotify
```

### How To Run
`python script.py`

### Response
<img src="https://github.com/Sunil02324/SonyLiv-Live-Notifier/blob/master/sample.png?raw=true" alt="Alt Text">

---


Please open a Issue if you are facing any problems.
