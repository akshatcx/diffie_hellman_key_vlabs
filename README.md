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
    - Arguments `bits`: One more than the number of bits expected in the generated value
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
- geng(l): Generates a prime number of l-1 bits
- calg(a,b,p): Returns the value of (a^b)%p


