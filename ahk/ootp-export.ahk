#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

WinActivate Out of the Park Baseball
Sleep 1000

Loop, 54
{
    MouseMove, 1135,481
    Sleep 250
    Click, down
    Sleep 250
    Click, up
    Sleep 250

    MouseMove, 1187, 530
    Sleep 250
    Click, down
    Sleep 250
    Click, up
    Sleep 250

    WinActivate Out of the Park Baseball
    Sleep 1000

    MouseMove, 3745,485
    Sleep 250
    Click, down
    Sleep 250
    Click, up
    Sleep 250
}



