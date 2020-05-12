# teachablemachine_airtable_EV3
<details>
<summary> #Setting up the html file:</summary>
<details>
<summary>1.	Train your Teachable Machine code. </summary>

</br>
</br> 
Go to https://teachablemachine.withgoogle.com/ and click on Get Started button

![Getting started](/images/getstarted.png)

</br>
</br>
</details>
 
<details>
<summary> 2.	Select the Audio Project</summary>


![audio project](/images/audioproject.png)

</br>
</br>
</details>
 
<details>
<summary>3.	Record sounds to train your model  </summary>

</br>
</br> 
Click on the microphone button to start recording. Record more samples for accuracy. Then click the Train Model button.
![trainingscreen](/images/trainingscreen1.png)

</br>
</br>
</details>


<details>
<summary>4. Export your Model.  </summary>

</br>
</br> 
Once you have recorded all samples and trained your data, click Export Model.
![trainedscreen](/images/trainedscreen.png)

</br>
</br>
</details>


<details>
<summary>5. Get the model url  </summary>

</br>
</br> 
Click on the Upload/Update my cloud model to create or update your model url. Copy the url from this page. 
![update](/images/update.png)

</br>
</br>
</details>

<details>
 
<summary> 5.	Edit the TeachableMachine.html file. </summary>

</br>
</br> 
Download and right-click and open the TeachableAudio.html file in a text editor like Sublime Text or VSCode. 
Paste the model url in the URL line. 
Similarly, Obtain APIKey and BaseID for your Airtable document and replace the text for APIKey and BaseID variables.

</br>
</br> 

![apiupdate](/images/updateapi.png)

</br>
</br>
</details>
</details>

<details>
<summary> #Using the html file:</summary>
 </details>
