# Rotation Order

- Michael N
- Christian
- Lisi 
- Florian D


# Goals

- [ ] Get mob tool running for whole team
    - [ ] might be necessary to run git bash from windows cmd
- [ ] Decide which problem to tackle

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
    
     