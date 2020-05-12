# airtable


<details>
<summary>Creating account - Creating Base </summary>

<h3> 1. Go to https://airtable.com </h3>
</br>
</br> 

![login screen](/images/airtable_welcome.png)

</br>
</br>

<h3> 2. Sign in if you have an Airtable account, or Sign up to create a new account</h3>
</br>
</br> 

![sign up screen](/images/signup.png)![sign in screen](/images/signin.png)

<h3> 3. Click on Add a base and Start from scratch   </h3>     

![add base screen](/images/addbase.png)

<h3> and give it a suitable name</h3> 

![name base screen](/images/namebase.png)
        
<h3> 4. This will open up your new document . Note the names of the Table and Fields </h3>
        
![table view screen](/images/tableview.png)
</details>



<details>
  <summary>Finding the BaseID </summary>

<h3> 1. Go to https://airtable.com/api </h3>

![api welcome screen](/images/apiwelcome.png)

<h3> 2. Click on your project name to reveal the api page. Copy the BaseID and replace the "BaseID" in secrets.py with this string </h3>

![api page screen](/images/apipage.png)

</details>



<details>
  <summary>Creating the API Key</summary>


<h3> 1. Go to https://airtable.com/account and click Generate API Key</h3>

![api welcome screen](/images/apikey1.png)

<h3> 2. Copy the API Key and replace the "AirtableAPPKey" in secrets.py with this string. Do not share this string.</h3>

![api welcome screen](/images/apikey2.png)

</details>

# teachablemachine_airtable_EV3
<details>
 
<summary> Setting up the html file:</summary>

 <details>
 <summary> 1.	Train your Teachable Machine code. </summary>

 <br>
 <br> 

 Go to https://teachablemachine.withgoogle.com/ and click on Get Started button

 <br>
 <br> 

 ![Getting started](/images/getstarted.png)

 <br>
 <br> 
 </details>

 <details>

 <summary> 2.	Select the Audio Project</summary>

 <br>
 <br> 

 ![audio project](/images/audioproject.png)

 <br>
 <br> 

 </details>

 <details>

 <summary> 3.	Record sounds to train your model  </summary>

 <br>
 <br> 

 Click on the microphone button to start recording. Record more samples for accuracy. Then click the Train Model button.

 <br>
 <br> 

 ![trainingscreen](/images/trainingscreen1.png)

 <br>
 <br> 

 </details>

 <details>

 <summary> 4. Export your Model.  </summary>

 <br>
 <br> 

 Once you have recorded all samples and trained your data, click Export Model.

 <br>
 <br> 

 ![trainedscreen](/images/trainedscreen.png)

 <br>
 <br> 

 </details>

 <details>

 <summary> 5. Get the model url  </summary>

 <br>
 <br>  

 Click on the Upload/Update my cloud model to create or update your model url. Copy the url from this page. 

 <br>
 <br> 

 ![update](/images/update.png)

 <br>
 <br> 

 </details>

 <details>

 <summary> 6.	Edit the TeachableMachine.html file. </summary>

 <br>
 <br>  

 Download and right-click and open the TeachableAudio.html file in a text editor like Sublime Text or VSCode. 
 Paste the model url in the URL line. 
 Similarly, Obtain APIKey and BaseID for your Airtable document and replace the text for APIKey and BaseID variables.

 <br>
 <br> 

 ![apiupdate](/images/updateapi.png)

 <br>
 <br> 

 </details>

</details>

<details>
 
<summary> Using the html file:</summary>
 
<br>
<br> 

After editing the html file with model url, APIKey and BaseID open it on your browser and hit start button. 
If it hears one of your trained models it creates a record on the Airtable document.


<br>
<br> 

<i> proceed with caution from here on...</i>

<br>
<br> 

The Airtable document is  updated only when a different sound is registered. For example, if I have a model to detect snapping and ticking sound and I snap twice subsequently Airtable will  be updated with only one snap record. In other words, the Airtable will only register the change in the input audio.  This is done to avoid unnecessarily creating too many records. 

<br>
<br> 

If you would like to record all the sound results then simply remove the section below with sendData(classLabels[highestIndex]);

![apiupdate](/images/code.png)
 
 </details>
