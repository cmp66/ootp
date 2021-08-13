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

GetSingleTournamentStats()
{
    MoveClickWait(1925,1448,1000)  ; remove win dialog
    MoveClickWait(996, 140, 500) ; main tournament menu
    MoveClickWait(996, 400, 1500) ; statistics
    MoveClickWait(1246, 369, 1500) ; sortable stats

    MoveClickWait(168, 486, 1000) ; views select
    MoveClickWait(132, 1018, 2000) ; batting view
    MoveClickWait(411, 473, 1000) ; filter select
    MoveClickWait(422, 697, 2000) ; batting filter
    MoveClickWait(1398, 486, 1000) ; report select
    MoveClickWait(1456, 551, 1000) ; write report to disk

    Sleep 3000

    WinActivate Out of the Park Baseball

    MoveClickWait(168, 486, 1000) ; views select
    MoveClickWait(132, 1092, 2000) ; pitching view
    MoveClickWait(411, 473, 1000) ; filter select
    MoveClickWait(430, 732, 2000) ; pitching filter
    MoveClickWait(1398, 486, 1000) ; report select
    MoveClickWait(1456, 551, 1000) ; write report to disk

    Sleep 3000

    WinActivate Out of the Park Baseball

    MoveClickWait(457, 135, 1000) ; main
    MoveClickWait(540, 602, 1000) ; ootp start screen

    Sleep 10000



}

GetAllTournamentStats(count)
{
    base_x := 2883
    base_y := 450

    Loop, %count%
    {
        adjust_y := (A_Index-1)*45
        MoveClickWait(2200, 1187, 3000) ; tournaments
        MoveClickWait(1733, 161, 2000) ; your tournaments
        MoveClickWait(base_x, base_y+adjust_y, 15000) ; goto the next tournament
        GetSingleTournamentStats()
    }
}

GetAllTournamentStats(30)

Esc::ExitApp