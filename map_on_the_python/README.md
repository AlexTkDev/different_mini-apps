# Project: Python Map using Folium
## Description
This project creates an interactive map using the Folium library. The map displays a marker at a given point, with the ability to add a popup with text.

## Installation
You will need Python 3.7 or higher to work with the project. Follow the instructions below to install all the necessary dependencies.

### Step 1: Clone the repository
Clone the repository to your local machine using Git:

```bash
git clone https://github.com/AlexTkDev/different_mini-apps.git
cd different_mini-apps
```

### Step 2: Create a virtual environment
It is recommended to create a virtual environment to install dependencies:

```bash
python -m venv .venv
```

### Step 3: Activate the virtual environment
Activate the virtual environment:

- **For Windows:**
```bash
.venv\Scripts\activate
```

- **For macOS/Linux:**
```bash
source .venv/bin/activate
```

### Step 4: Install dependencies
Install the required dependencies from the file `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Dependencies
The project uses the following main dependencies:
- `folium==0.14.0`: A library for creating interactive maps in Python.
- `ipython`: For displaying maps in Jupyter Notebook or IPython.

## Running the project
To run the project, use the following command:

```bash
python -m main
```
After executing the command, an interactive map will be created, which can be saved to the `map.html` file.

### Saving and viewing the map
The map is saved to the `map.html` file. Open this file in a browser to view it.
Open the `map.html` file in a browser to see the map.

## Project Structure

```plaintext
your-repo-name/
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

- `main.py`: The main project file, containing the code to create and display the map.
- `requirements.txt`: The project dependencies file.
- `README.md`: The project documentation.

### Contributions
If you have ideas for new widgets or improvements to existing ones, you can create a pull request or open an issue in the repository.

### Notes:
- **central_park_location**: Coordinates of Central Park.
- **my_map**: Map opens with focus on Central Park.
- **CircleMarker and Marker:** Add a visual marker and popup on the map at the location of 
  Central Park.

