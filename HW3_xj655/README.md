# HW3-1
+ delet assignment: which is to delet the sensitive data file both from history and data file. 
When set up a new csv file, I pull it from the github to local computer and run two codes in terminal:
>git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch HW3_xj655/Lab3_xj655/test.csv’ --prune-empty --tag-name-filter cat -- --all
>git push origin    --  force  --all

I put all the material in  subfolder Lab3_xj655
The screen shot of history before deleting is
![Alt text]()
![Alt text]()
The screen shot of history after deleting is
![Alt text]()

# HW3-2
Read the data from NYC open data csv link and json API and to do the preliminary purifying and ploting
()


# HW3-3
+ [show_bus_location_xj655.py]()
This py file  scraped data through API key to get the real-time bus line data info
To run the file, put the following code in terminal
>py show_bus_location_xj655.py   <API KEY>   <BUS LINE> 

# HW3-4
+[get_bus_info_xj655.py]()
This py file scrape ata through API key to get the real-time next stop bus info,  and the output is a csv file list the info. Need one more input than HW3-3
>py get_bus_info_xj655.py <API KEY>  <BUS line> <BUS LINE.csv>

##All api key need to be applied through the following step:
Visit MTA Bus Time for Developers at the [MTA Developers Tools](http://bustime.mta.info/wiki/Developers/Index)
Click on the “Go here” link to fill in your information and request an API. You should be receiving an email from MTA within an hour (most of the time within only a few minutes).
The key should be in the form of xxxxx-xxxxx-xxxxx-xxxxx-xxxxx. Please keep this key only to yourself as it would be your authorization token for MTA access and will be in this assignment.
