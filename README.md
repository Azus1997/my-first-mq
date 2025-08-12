This is a Public Repository to train and dispĺay my Rabbit MQ skills (if any).

It's Football time! Start the match and turn on the radio! You will hear every goal in this fierce competition.

Watch me try to leverage Python, RabbitMQ, Bash and Docker to excecute the most basic Messaging exercice out there in a classic example of over engineering.
As well as trying to create a legitimate and understandable documentation of what is supposed to be a half hour excercise.

Here we go:
My-first-MQ (My First Message Queue) is my first excercise in attempting to use Rabbit MQ.

The idea behind it was to alow me to start learning Microservices Architecture at a practical level.
I chose to use Python in this case as its a language I have some familiarity with but not as much as I'd like, so any little bit helps.
Somewhere down the line I decided *"Yes, it IS a great idea to implement Docker to make sure that running this app is as easy as can be for anyone!"* -woah boy, that derailed the whole "mainly learning MQ" thing quickly. I ended up struggling most trying to get my app container to use the Rabbit MQ server from the other container, mostly because i had no idea how to write a Compose file.... or what a Compose file was, for that matter. But now that I have (HOPEFULLY) succeeded, running this app should be as simple as:
 1. Cloning the repo
 2. opening a terminal
 3. changing the location to the cloned repo's folder
 4. running the following command
 ´´   docker compose up -d

Unfortunately this does mean that **Docker IS a requirement**. But if I didn´t mess things up, nothing else should be.

Feel free to clone, try it out, send me ludicrous amounts of money and/or brake it or fix it to your heart's contempt.

In all seriousness Ill appreciate any feedback you might have, and thank you for reading!

Have an awesome day.
