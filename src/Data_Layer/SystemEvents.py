class SystemEvents:
    # NOTE: Format: xxff - xx determines the type of event where ff is the id.
    #               xx = 10 for input events
    #               xx = 11 for window events
    #               xx = 12 for game events

    MOUSE_CLICK             = 1001
    UP_PRESSED              = 1002
    DOWN_PRESSED            = 1003
    RIGHT_PRESSED           = 1004
    LEFT_PRESSED            = 1005
    KEY_RELEASE             = 1006
    RETURN_PRESSED          = 1007
    PAUSE_PRESSED           = 1008
    TERMINATE_GAME          = 1101
    STATE_TRANSITION        = 1201
    MAZE_UPDATE             = 1202
    DIFFICULTY_EASY         = 1203
    DIFFICULTY_MEDIUM       = 1204
    DIFFICULTY_HARD         = 1205
    LEVEL_RESET             = 1206
    REQUEST_LEVEL_GENERATE  = 1207
    TIME_UPDATE             = 1208
    LEVEL_FINISHED          = 1209
    LEVEL_NEXT              = 1210
    PLAYER_WIN              = 1211
