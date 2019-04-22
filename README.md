# IIITH Intro To Software System (Spring 2019)
This project is a part of an assignment for the ISS course.

## Steps to Run
- Run `git clone https://github.com/akshatcx/diffie_hellman_key_vlabs` to clone.
- Run `virtualenv env` to create a python virtual environment for the project.
- Run `pip3 install -r requirements.txt` to install all the dependencies.
- Move into the app directory using `cd app`
- Run `flask run` to run the app in your localhost.
- Visit `localhost:5000` on the browser to access the website.

## API reference
- `/api/genp`
    - Arguments `bits`: No of bits expected in the generated value
    - Returns `prime`: A randomly generated prime number with the required amount of bits  

- `/api/geng`
    - Arguments `prime`: Value of the main prime
    - Returns `generator`: A randomly generated prime number smaller than the original prime
- `/api/private_key`
    - Arguments `prime`: Main prime number in the experiment
    - Returns a private key which is a random number less than prime

- `/api/calg`
    - Arguments
        - `p`: Prime value
        - `g`: Generator value
        - `a`: Private key 1
        - `b`: Private key 2

    - Returns
        - `Ga`: (g^a)%p
        - `Gb`: (g^b)%p
        - `Gab`: (Gb^a)%p
        - `Gba`: (Ga^b)%p
        
## Database Reference
- The database stores the answers submitted to the quiz along with the timestamps
- Route to see the answers: `/answers` 

## Helper functions (in `app/api/helper.py`)
- genp(l): Generates a prime number of l bits
- geng(p): Generates a prime number lesser than p
- calg(a,b,p): Returns the value of (a^b)%p

## Design Pattern (Model-View-Controller Pattern)

### Design
- Model: Represents the object carrying all the raw data. In this case it is the implementation of the SQLAlchemy Database.
- View: Represents the visualization of the data that model contains. It includes everything that the user sees when he/she interacts with the application. In this case it contains all the HTML files (templates) which are shown to the user in the front-end side.
- Controller: Controller works on the view and the model and acts like a bridge between them. It listens to events triggered by the view and executes the appropriate reaction to these events. In this case in contains all the logic behind the experiment. Moreover it also controls which method is called when a particular button is pressed.

### Advantages
- Multiple developers can work simultaneously on the project with minimal conflicts.
- Makes the project modular in nature
- Enables logical grouping of related actions on a controller together
- The data is stored without the the need of formatting


