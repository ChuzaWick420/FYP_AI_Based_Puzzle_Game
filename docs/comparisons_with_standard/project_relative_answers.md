# Project relative answers compared to standard
This document compares and answers concerns mentioned in [considerations for producing a good SRS](./considerations.md).

## Nature of the SRS
### Functionality
The product (i.e. software) is supposed to 
- demonstrate engineering skills learnt throughout the university's courses.
- be playable without bugs and crashes.
- be evaluated by supervisor.

### External Interfaces
The software
- interacts with (people)
  - supervisor for evaluation.
  - colleagues for sharing ideas.
  - friends for show casing.
- interacts with (system's hardware)
  - keyboard for playing.
  - screen for observing game updates.
  - (EXTRA) speakers for audio.
  - system resources such as
    - CPU for computation.
    - RAM for storing data.
    - Disk for 
      - Keeping track of scoreboards.
      - (EXTRA) loading sprites.
- doesn't interact with additional hardware external to the computer system.
- interacts with (other software)
  - operating system
    - windows
    - (EXTRA) linux
  - `Python` interpreter
  - Modules / Libraries such as
    - `random`
    - `time`
    - `pygame`

### Performance
- Game should run at 30 frames per second at least.
- Controls should be responsive enough to enjoy the game.
- Maze generation should take less than 10 seconds.
- Path finding should take less than 10 seconds.

### Attributes
#### Portability
The software package will contain only
- source code
- (EXTRA) sounds
- (EXTRA) sprites

#### Correctness
##### Mathematics
The product will _not_ follow mathematical rigor, although it will use the mathematical objects.

##### Programming Conventions
The product will 
- _not_ follow any styling conventions such as the ones from Nasa or Google. 
- adhere to Object Oriented Principles.

##### Requirements
The product will deliver all the functional requirements alongside necessary implicit non functional requirements.

##### Design Constraints imposed on an implementation
- Implementation language will be `Python`.

## Environment of the SRS
The features marked as `(EXTRA)` should go into documents like software quality assurance plan instead of SRS document.
