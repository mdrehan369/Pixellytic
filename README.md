# Pixellytic

Pixellytic is an application which uses techniques of Machine Learning to simplify image searching.

# Description

Pixellytic is an application made from Python and its GUI libraries. 
The front end is done by Customtkinter, a modern version of Tkinter developed by Tom Schimansky.
You can find its repo in Git Hub. It uses a library Scikit Learn famous for machine learning and uses it to distinguish images.

To use it, first, you have to train your image machine-learning model. To do so collect some images of the subject and store them in a folder. There should be at least 20 to 30 pictures in different environments and outfits. Then run the app, choose "Add Model" specify the name of the model, and browse to the folder where you saved your sample images and train it.

After training, it's time to use our model. Navigate to "Use Model" then specify the model that you want to use and then specify the folders where you want to use it and where you want to store the extracted images.

Your model will extract subject images from the specified folder and store them in the other folder.

## Installation
To install Pixellytic, make sure that you have git and python install in your local machine.

First clone this repository.
```bash
git clone https://github.com/mdrehan369/Pixellytic.git
```
After cloning open the terminal and install the required packages using [pip](https://pip.pypa.io/en/stable/) and requirements.txt

```bash
pip install -r requirements.txt
```

At the last, just write the following command to run the program
```bash
python app.py
```
Note: if any error occured use the terminal with administrative privilages. In case of linux , use python3 and pip3 in place of python and pip.

## Usage

If you want to increase your model accuracy, try to give more sample images with only the subject image and not group photos.

## License

[MIT](https://choosealicense.com/licenses/mit/)