# cccBot
pynput bot that does the code completion for u


!! This bot only automates the copy paste process, it does not write actual code !!

1. Open your [LMS Portal](https://icode.ccc.training/) and choose the required course. Complete the MCQs and keep the CODING questions ready.

2. Add [Text Blaze](https://chrome.google.com/webstore/detail/text-blaze/idgadaccgipmpannjkmfddolnnhmeklj) extension to your browser for text expansion  
  In Text Blaze, sign in and make a new snippet. This is where the bot will copy and paste the codes from since the lms portal does not allow you to paste the answer on their site. The default snippet keyword is **/do**. DO NOT CHANGE THIS

3. Keep both the LMS tab and the Text Blaze tab open in one browser window. YOU SHOULD BE ABLE TO CTRL+TAB BETWEEN THE TWO SITES.

4. Download the main.py python file from this repository.  
  Go to main.py, click RAW, ctrl+s
  
5. Install pynput from your terminal
```
pip install pynput
```

6. Run the code from your terminal  
  Open your terminal and locate where you saved main.py, and run using python.  
  ex:  
  ```
  C:\Users\abhi>cd desktop

  C:\Users\abhi\Desktop>python main.py
  ```
  if python is not found, try python3.
  
7. Esc out of fullscreen mode if you are in fullscreen. Make sure ur browser zoom level is on 100% and not anything else.  
  As soon as u run the code, hover your mouse (DONT CLICK) over the "Check answers" button, then over the "Next" button and then over the "Submit Code" button, each for 2 seconds.  
  It is advisable that you keep your terminal open as a small window on your screen for this step so that you can see the prompts and know when to change buttons.  
  Type in the number of CODING questions after the prompt, hit enter,  and MAXIMISE YOUR BROWSER WINDOW. (do not go fullscreen) 

8. If all steps are done correctly, the bot should start automating the process for you.

9. To interrupt the bot, go to ur terminal and press ctrl+c  (this may be tricky when the bot is still running)


WARNING:
* Some questions have solutions which have more than 2500 characters. The free version of Text Blaze does not support them and hence these codes will not compile properly. You will manually have to fill in these questions.

* Some questions have a different language set up by default. Make sure the questions are in C++(17) / Java(11) according to the given answer.

* Some questions just dont work or take too long to compile. This is the LMS portal's fault and you will need to do those questions manually.

* You will generally get above 50% from the bot alone, which is enough to pass ( i think)

  
  
