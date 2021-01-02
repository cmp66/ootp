#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
#SingleInstance force
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


Sleep 5000 ;this needs to be here to allow init functions to complete


WinActivate Out of the Park Baseball
Sleep 1000

SelectExportType(y) 
{
    MouseMove, 115, 485 
    Sleep 250
    Click, down
    Sleep 250
    Click, up
    MouseMove, 112, y
    Sleep 250
    Click, down
    Sleep 250
    Click, up
    Sleep 250

    Sleep 2000
}

SelectFilterType(y) 
{
    MouseMove, 304, 484 
    Sleep 250
    Click, down
    Sleep 250
    Click, up
    MouseMove, 304, y
    Sleep 250
    Click, down
    Sleep 250
    Click, up
    Sleep 250

    Sleep 2000
}

ToggleIntPlayers() 
{
    MouseMove, 567, 435 
    Sleep 150
    Click, down
    Sleep 150
    Click, up
    Sleep 150

    Sleep 2000
}

ToggleMLPlayers() 
{
    MouseMove, 302, 435 
    Sleep 150
    Click, down
    Sleep 150
    Click, up
    Sleep 150

    Sleep 2000
}

ExportOOTPRatings(x)
{
    MouseMove, x,481
    Sleep 250
    Click, down
    Sleep 250
    Click, up
    Sleep 250

    MouseMove, x, 530
    Sleep 250
    Click, down
    Sleep 250
    Click, up
    Sleep 250

    WinActivate Out of the Park Baseball
    Sleep 1000
}

ResetPageIndex(resetoffset)
{
    MouseMove, resetoffset, 490
    Sleep 250
    Click, down
    Sleep 250
    Click, up
    Sleep 250
}

ExportOOTPRatingsPaging(x, pagecount, resetoffset)
{
    Loop, %pagecount%
    {
        ExportOOTPRatings(x)

        MouseMove, 3745,485
        Sleep 250
        Click, down
        Sleep 250
        Click, up
        Sleep 250
    }

    ResetPageIndex(resetoffset)
}


; all player
; ToggleMLPlayers()
; ToggleIntPlayers()
; SelectExportType(1417) ; Player Export
; ExportOOTPRatingsPaging(1040,235, 3503)
; SelectExportType(1385) ; Batter Export
; ExportOOTPRatingsPaging(1040,235, 3503)
; SelectExportType(1453) ; Fielding Export
; ExportOOTPRatingsPaging(1040,235, 3503)
; SelectExportType(1502) ; Pitching Export
; ExportOOTPRatingsPaging(1040,235, 3503)
; ToggleMLPlayers()
; ToggleIntPlayers()

; SelectFilterType(1103) ; MLB
; SelectExportType(1417) ; Player Export
; ExportOOTPRatings(1070)
; SelectExportType(1385) ; Batter Export
; ExportOOTPRatings(1070)
; SelectExportType(1453) ; Fielding Export
; ExportOOTPRatings(1070)
; SelectExportType(1502) ; Pitching Export
; ExportOOTPRatings(1070)

; ToggleIntPlayers()
; SelectFilterType(1142) ; INT
; SelectExportType(1417) ; Player Export
; ExportOOTPRatings(1070)
; SelectExportType(1385) ; Batter Export
; ExportOOTPRatings(1070)
; SelectExportType(1453) ; Fielding Export
; ExportOOTPRatings(1070)
; SelectExportType(1502) ; Pitching Export
; ExportOOTPRatings(1070)
; ToggleIntPlayers()

ToggleMLPlayers()

SelectFilterType(1179) ; FS
SelectExportType(1417) ; Player Export
ExportOOTPRatingsPaging(1150,67, 3530)
SelectExportType(1385) ; Batter Export
ExportOOTPRatingsPaging(1150,67, 3530)
SelectExportType(1453) ; Fielding Export
ExportOOTPRatingsPaging(1150,67, 3530)
SelectExportType(1502) ; Pitching Export
ExportOOTPRatingsPaging(1150,67, 3530)

SelectFilterType(1212) ; SS
SelectExportType(1417) ; Player Export
ExportOOTPRatingsPaging(1150,51, 3530)
SelectExportType(1385) ; Batter Export
ExportOOTPRatingsPaging(1150,51, 3530)
SelectExportType(1453) ; Fielding Export
ExportOOTPRatingsPaging(1150,51, 3530)
SelectExportType(1502) ; Pitching Export
ExportOOTPRatingsPaging(1150,51, 3530)

ToggleMLPlayers()

Esc::ExitApp






