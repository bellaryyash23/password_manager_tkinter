# 🔒Password Manager App using Tkinter of Python

🌟A GUI based app which helps you generate, search and manager your passwords from various websites on your local system. 

🌟The app generates passwords which are hard to decode ensuring safety from password leak or hacking and 
since, the passwords are stored on your local systems it ensures privacy & no loss of your data.

👉The UI setup of the app is done using the tkinter classes like Label, Button, Tk, Entry, PhotoImage and Canvas.

👉The Canvas class is used to design the background image of the app. 

👉The objects are placed and packed on the window using the .grid(..) method of the tkinter class which divides the whole window into 
rows and columns. The attribute columnspan is used for effective design and placement of labels and buttons.

![Start Window](https://github.com/bellaryyash23/password_manager_tkinter/blob/master/start.JPG?raw=true)

👆Start Window of the App👆

🔒Password generation mechanism:

👉In the App, the user adds the website name for which the password details are to be generated. Once all the required fields are entered, the user can press the
'Generate Password' which generates a highly secure and hard to decode password using the 'generate_password' function. 

👉The generated password is copied onto the clipboard of the user for easy usuage. This functionality is implemented using the 'pyperclip' package of python 
which provides this functionality of copying and pasting texts onto the clipboard.

![Generate Password Window](https://github.com/bellaryyash23/password_manager_tkinter/blob/master/generate.JPG?raw=true)

👆App window after Password Generation👆

🔒Password saving and adding mechanism:

👉Once generated the user can save these details for future use on their local system by clicking on the 'Add' button. This will call the 'save' function which
extracts the data entered by user in the respective fields and converts them into a dictionary.

👉In beta version the app used 'data.txt' to save the user details but, on the updated version the use of json format for effective and efficient data storage
is implemented.

![Text data file](https://github.com/bellaryyash23/password_manager_tkinter/blob/master/txt_data.JPG?raw=true)

👆Data stored in text file👆

👉Hence, in the 'save' function, the extracted data converted to python dictionary is added to the 'data.json' file. The in-built json module of Python is used for
data handling and updation in the json file. The use of error handling ensures an proper functionality of the app. Also, the use of json formatting helps in data
searching, data visualization and data updation which, is another functionality of the app.

![Json data file](https://github.com/bellaryyash23/password_manager_tkinter/blob/master/add_data.JPG?raw=true)

👆Data stored in Json file👆

🔒Password searching mechanism:

👉The app provides the user with the added functionality to search the previously added data and obtain the password using the website name as a query. Thus, user 
must enter the proper website name and press the 'Search' button which calls the 'search_password' function.

👉Inside 'search_password' function, the website entry field value is extracted and used as a key to find the other values. Here, due to the use of json file 
format of the 'data.json' file the searching becomes easy and efficient. The found values are displayed to user via a prompt and on the user's confirmaton 
the password is copied onto the clipboard using the 'pyperclip' package of Python as mentioned earlier.

![Search Result window](https://github.com/bellaryyash23/password_manager_tkinter/blob/master/search.JPG?raw=true)

👆Search result window👆

🔒Error handling mechanism:

👉For proper and hassle-free functioning of the app the use of in-buit error Python handling function is done. This makes the app working smooth and effective
for the user.

👉Also the user of error prompts of the tkinter class provide proper feedback to the user and make the working of the app bug free. 

![Error handling of the App](https://github.com/bellaryyash23/password_manager_tkinter/blob/master/error.JPG?raw=true)

👆Error handling of the app👆

🌟In this way, the password manager apps effective functioning is achieved.
