;my basic emacs config
(require 'package)
(add-to-list 'package-archives
       '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)
(package-refresh-contents)

;installed packages
(defvar myPackages
  '(better-defaults
    cyberpunk-theme
    ivy
    elpy
    beacon
    ace-window
    ))

;making sure packages are installed
(mapc #'(lambda (package)
    (unless (package-installed-p package)
      (package-install package)))
      myPackages)
 
;extra keybinds
(global-set-key (kbd "M-n")
       	(lambda () (interactive) (next-line 5)))
(global-set-key (kbd "M-p")
       	(lambda () (interactive) (previous-line 5)))
(global-set-key (kbd "M-;") 'previous-buffer)
(global-set-key (kbd "M-'") 'next-buffer)
(global-set-key (kbd "M-|") 'append-to-buffer)
(global-set-key (kbd "M-o") 'ace-window)
(setq aw-keys '(?a ?s ?d ?f ?g ?h ?j ?k ?l))

;spellcheck
(dolist (hook '(text-mode-hook))
  (add-hook hook (lambda () (flyspell-mode 1))))

;line numbers
(line-number-mode t)
(global-display-line-numbers-mode)
(column-number-mode t)

;ivy
(ivy-mode 1)

;elpy
(elpy-enable)

;Beacon
(beacon-mode 1)

;python shell
(setq python-shell-interpreter "python3")

;inhibit startup msg
(setq inhibit-startup-message t)

;load custom theme
(load-theme 'cyberpunk t)
