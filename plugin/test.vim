function! Create()
if !has('python')
    echo "error"
    finish
endif
:belowright split HUD
:set nonu
:25winc-
:set laststatus=0
:setlocal buftype=nofile
:call Update()
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
    loadedLibs = True
except ImportError:
    print "need recommender in pythonpath"
    
if loadedLibs:
    vim.buffers[2].append("j=down, k=up, l=right, h=left, Esc=normal mode, i=insert mode")
    x = recommender.recommend()
    del vim.buffers[2][0]
    del vim.buffers[2][0]
    vim.buffers[2].append("%s"%x)
EOF
endfunction 

autocmd CursorHold * call Timer()
function! Timer()
call feedkeys("f\e")
call Update()
endfunction
:call Create()
