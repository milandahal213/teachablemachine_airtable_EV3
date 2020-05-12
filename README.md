# teachablemachine_airtable_EV3
<details>
 
<summary> Setting up the html file:</summary>

<details>
<summary>1.	Train your Teachable Machine code. </summary>

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
 
<summary>3.	Record sounds to train your model  </summary>

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
 
<summary>4. Export your Model.  </summary>

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
 
<summary>5. Get the model url  </summary>

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
 
<summary> 5.	Edit the TeachableMachine.html file. </summary>

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
