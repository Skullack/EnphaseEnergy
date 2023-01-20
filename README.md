# EnphaseEnergy Automation
Python Scripts For Enphase Enlighten Automation with Selenium.
You will need to replace "youremailaddress" and "yourpassword" in the scripts to be able to login to enphase elighten and run the scripts.

I created these Selenium Python scripts out of frustration because Enphase provides no support for running commands against their API's. I wanted to be able to set a schedule that automatically switches my battery profile between FullBackup and SelfConsumption. 
I am aware that SelfConsumption kicks in when their is no SUN light. I wanted it to kick in later in the night because I first wanted to make use of my excess solar power sent to the grid. We have a "use it or lose it" setup, so nothing is carried over to the next month therefore I have to use that excess. 
For same minded individuals my schedule is setup as follows. 
1. SelfConsumption kicks in at 11pm.
2. FullBackup kics in at 8am 
3. excess power left from the previous day is used to charge the batteries.
By the time the sun is providing enough power my batteries are fully charged and the excess goes back to the grid again to follow same procedure.
This method makes us 97% energy efficient.

I am running this via Windows and you would need to make the required changes to run in Linux which should be very easy to do. 

Requirements.
You need to install WebDriver for your browser version.
You need to install Selenium.
I dont think this will work in Python 2.7. I did not test it as I used Python 3.8
