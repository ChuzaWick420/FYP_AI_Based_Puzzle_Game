class SystemEvents:
    # NOTE: Format: xxff - xx determines the type of event where ff is the id.
    #               xx = 10 for input events
    #               xx = 11 for window events
    #               xx = 12 for game events

    MOUSE_CLICK      = 1001
    TERMINATE_GAME   = 1101
    STATE_TRANSITION = 1201
