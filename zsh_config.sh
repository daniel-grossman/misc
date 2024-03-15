eval "$(/opt/homebrew/bin/brew shellenv)" 

#aliases
alias res='exec zsh'
alias ls='ls -oahG'
alias em='emacs'
alias py='python3'
alias ipy='ipython'
alias brewup='brew update && brew upgrade && brew cleanup'
alias add='hledger add'
alias bal='hledger balance'
alias print='hledger print'
alias exp='hledger bal -M expenses -2 -SA'
alias bs='hledger bs -tS'
alias is='hledger is -tS'
alias bsv='hledger bs --flat -VtS'
alias sha='shasum --algorithm 256'
alias ver='gpg --verify'
alias md='mdls -name kMDItemVersion'
alias mda='for file in *; do echo "$file: $(md "$file")"; done'
alias exif='exiftool'
alias exifr='exiftool -all:all= -r'
alias yt='yt-dlp -f bestaudio -x --audio-format mp3 --audio-quality 320k --embed-thumbnail'

#cs function
function cs () {
    cd $1
    ls
}
