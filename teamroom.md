
# Get mob tool & git working FGR:

- I'm now on master branch, therefore lets try to push this change via GUI to master branch!
   - That just worked fine! No pwd or user name request
- Well, lets try this via git bash!
   - Not working well so far. I'm asked for user name and pwd again. More details see "Miro"
- Try help from stackOverflow regarding credential:
    - in git bash type: "git config --global credential.helper wincred"
    - Time to push again, this should ask once more for credential
       - It asked for credentials again
    - No lets try to push again and see if credentials are still required
       - "Ja sauber die Musi!" Success! no credentials asked for!
    - CONCLUTION: at least credential manager link was missing.
- It's time for mob start/mob next
    - Lets push current changes before "mob start"
    - It is working!
