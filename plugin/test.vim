function! Create()
if !has('python')
    echo "error"
    finish
endif
:belowright split HUD
:set nonu
:35winc-
:set laststatus=0
:setlocal buftype=nofile
:call Start()
endfunction

function! Start()
if !has('python')
    echo "error"
    finish
endif
python << EOF
import vim
loadedLibs = False
try:
    import recommender
    bl = vim.buffers

    for buff in bl:
        if str(buff) == '<buffer HUD>':
            HUD = buff

    HUD.append("j=down, k=up, l=right, h=left, Esc=normal mode, i=insert mode\n")
except ImportError:
    print "need recommender in pythonpath"
EOF
endfunction 

function! Update()
if !has('python')
    echo "error"
    finish
endif
python << EOF
import vim
loadedLibs = False
try:
    import recommender
    bl = vim.buffers

    for buff in bl:
        if str(buff) == '<buffer HUD>':
            HUD = buff
    
    HUD.append("j=down, k=up, l=right, h=left, Esc=normal mode, i=insert mode\n")
    del HUD[0]
    del HUD[0]
    x = recommender.recommend()
    HUD.append("%s"%x)
except ImportError:
    print "need recommender in pythonpath"
EOF
endfunction 

autocmd CursorHold * call Timer()
function! Timer()
call feedkeys("f\e")
call Update()
endfunction

:call Create()
