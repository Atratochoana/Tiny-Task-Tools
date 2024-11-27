#Requires AutoHotkey v2.0

b::{
    MouseMove 67, 360, 50
    Click
}


g::{
    MouseGetPos &xpos, &ypos 
    MsgBox "The cursor is at X" xpos " Y" ypos
}

