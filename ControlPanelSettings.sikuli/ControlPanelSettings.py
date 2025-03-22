import os
from sikuli import *

keyDown(Key.WIN)
keyUp(Key.WIN)
wait(1)

paste("Control Panel")
wait(1)

type(Key.ENTER)

click(Pattern("HardwareAndSound.png").targetOffset(-52,-34))

click(Pattern("MobilityCenter.png").targetOffset(-41,-11))


click(Pattern("MuteCheckbox.png").targetOffset(-20,-36))

wait(1)

click(Pattern("cancelDialog1.png").targetOffset(310,-148))

click(Pattern("cancelDialog2.png").targetOffset(367,-279))

