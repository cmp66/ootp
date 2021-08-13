#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
#SingleInstance force
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


Sleep 5000 ;this needs to be here to allow init functions to complete

; All the screen coordinates


WinActivate Out of the Park Baseball
Sleep 1000

MoveClickWait(x, y, sleep)
{
    MouseMove, %x%, %y%
    Click, down
    Sleep 250
    Click, up
    Sleep %sleep%
}

MoveClickWait(2200, 1187, 2000) ; tournaments

Loop{
    WinActivate Out of the Park Baseball
    MoveClickWait(5074, 786, 1000) ; tournament ready
    MoveClickWait(1000, 300, 10000) ; refresh

    MoveClickWait(5074, 786, 1000) ; tournament ready
    MoveClickWait(2908, 454, 15000) ; submit

    MoveClickWait(2268, 1235, 2000) ; tourney ack

    MoveClickWait(5069, 773, 2000) ; ok in case set roster

    MoveClickWait(457, 135, 1000) ; main
    MoveClickWait(540, 602, 1000) ; ootp start screen

    Sleep 10000

    MoveClickWait(5074, 786, 1000) ; tournament ready

    MoveClickWait(2200, 1187, 2000) ; tournaments
}

Esc::ExitApp


