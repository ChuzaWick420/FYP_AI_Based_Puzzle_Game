class SystemEvents:
    # NOTE: Format: xxff - xx determines the type of event where ff is the id.
    #               xx = 10 for input events
    #               xx = 11 for window events
    #               xx = 12 for game events

    MOUSE_CLICK      = 1001
    UP_PRESSED       = 1002
    DOWN_PRESSED     = 1003
    RIGHT_PRESSED    = 1004
    LEFT_PRESSED     = 1005
    KEY_RELEASE      = 1006
    TERMINATE_GAME   = 1101
    STATE_TRANSITION = 1201
