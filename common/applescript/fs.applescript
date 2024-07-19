tell application "System Events"
    set frontApp to name of first application process whose frontmost is true
    tell application process frontApp
        if windows is not {} then
            set frontWindow to first window
            -- Get the screen dimensions using Finder
            tell application "Finder"
                set screenBounds to bounds of window of desktop
                set screenWidth to item 3 of screenBounds
            end tell
            set windowWidth to 1386
            set xPosition to screenWidth - windowWidth
            set position of frontWindow to {xPosition, 23}
            set size of frontWindow to {windowWidth, 900}
        else
            error "No windows found for the frontmost application."
        end if
    end tell
end tell
