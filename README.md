## GALLERY

 An application where users can view and search images of vehicles in accordance to their categories.

## TECHNOLOGIES USED

* Django
* Python
* HTML
* Bootstrap

## SET UP INSTRUCTIONS

* Clone the repo locally to your desired folder in your PC.
   ` git clone https://github.com/Emmanuel-9/Gallery `

* Open the cloned application in an IDE of choice such Sublime Text, VSCode and many others.

* Create a virtual environment to for the application. This can on the terminal using the command
  ` python3.6 -m venv --without-pip <name_of_the_virtual_environment> `
  If giving the virtual environment is a bit difficult, you can assign it the default name **VIRTUAL**
  
* Activate the created virtual environment 
  ` source virtual/bin/activate `

* In the activated virtual environment, install pip which would be used to install dependencies in Python, which can be using the   command: ` curl https://bootstrap.pypa.io/get-pip.py | python `

* Install the dependencies used in the application ` pip install -r requirements.txt ` , the command will the interpreter to
  install the dependencies in the file _requirements.txt_

* Run ` python3 manage.py runserver ` to run the application.


## AUTHOR
* Emmanuel Orega

## LICENSE
MIT License

Copyright (c) [2020] [Emmanuel Orega]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.