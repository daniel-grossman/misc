alias ls='ls -oahG'
alias 'brewup'='brew update && brew upgrade'
alias exif='exiftool'
function cs () {
    cd $1
    ls
}
