# Getting started with Airtable


<details>
<summary>Creating account on Airtable - Creating Base </summary>

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

# Setting up Teachable Machine on PC

Download the TeachableAudio.html file from <i> On PC </i> folder. 

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

 <summary> 6.	Running the TeachableAudio.html file. </summary>

 <br>
 <br>  

Open the TeachableAudio.html file on a browser of your choice. We have tested it on Chrome. 

Enter the url from Step 5 in the text box saying <i>url</i>.
Also enter the APIKey and BaseID for your  Airtable document in their respective boxes.
<br>
Refer to the sections <i> Finding the BaseID </i> and <i> Creating API Key </i> above on where to find them.


 <br>
 <br> 

 ![apiupdate](/images/html.png)

 <br>
 <br> 

 </details>

</details>

<details>
 
<summary> Optional: editing the html file:</summary>
 
<br>
<br> 
<i> please proceed with caution...</i>

If you want to edit the html file or want to see how the code is written,  right-click and open the html file on an editor. 

<br>
<br> 


 </details>
 
# Setting up the library on EV3

Download the airtable.py, secrets.py, demo.py and main.py file from <i> On EV3 </i> folder and save them on your projects folder on EV3.

<details>
  <summary>Using the library</summary>
   
<h3> 0. Download secrets.py and airtable.py to your EV3.</h3>


<h3> 1. Edit the secrets.py file</h3>

Edit the secrets.py file by replacing BaseID and API Key from your account. Refer to the sections <i> Finding the BaseID </i> and <i> Creating API Key </i> above on how to do it.

<h3> 2. Understand the demo.py file</h3>

The demo.py file contains information on how to use the available Airtable functions. You may not need to use all of them, but it is useful to know what else you can do. 

In summary, you will use Get_AT and Get_AT_field functions to read single or full set of records, you will use Put_AT to create a record and Delete_AT to delete a record.

<details>
<summary>Put_AT</summary>
        
Put_AT('Table_name','Field_name','Record_value') 
Put_AT function adds a record in the Field_name Field of the  Table_name Table with the value Record_value
The function returns the record id for the updated record (useful for deleting)

</details>
<details>
        
<summary>Get_AT</summary>

Get_AT('Table_name','Field_name') returns the last record from the Field_name Field of the Table_name Table.   

</details>
<details>
<summary>Get_AT_field</summary>
        
Get_AT_field('Table_name','Field_name') returns the entire list of record from the Field_name Field of the Table_name Table. The return value will be a list. Users will need to use indexing to access individual records. use [-1] to access the last record. 

</details>
<details>
<summary>Delete_AT</summary>

Delete_AT('Table_name',"record_id")  deletes the  record with "record_id" from the Table_name Table.

</details>

<h3> 3. Edit the main.py file</h3>

You can start playing with the library using main.py. It shows how you can import airtable library and use the available function. 


</details>
