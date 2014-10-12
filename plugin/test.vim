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
import recommender
import Parser
Parser.update()
x = recommender.test()
del vim.buffers[2][0]
vim.buffers[2].append("%s"%x)
EOF
endfunction

autocmd CursorHold * call Timer()
function! Timer()
      call feedkeys("f\e")
      call Update()
endfunction
