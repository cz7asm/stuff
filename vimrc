set tabstop=4
set shiftwidth=4
set softtabstop=4

set nowrap

set smarttab
set expandtab

set number
set ruler
set foldcolumn=1

set hlsearch
set incsearch
set ignorecase
set hidden
syn on
syntax sync fromstart

set foldmethod=syntax
set foldnestmax=1
set foldopen-=block
set nofoldenable

set smartindent
set backspace=indent,eol,start

"set path+=**

autocmd BufRead *.py inoremap # X#
autocmd BufRead *.py setl nosmartindent
filetype plugin indent on

let g:netrw_banner=0
let g:netrw_list_hide='^\.\w'
"let g:netrw_chgwin=1
nnoremap <silent> <S-CR> :rightbelow vs<CR>:e .<CR>

imap <C-BS> <C-W>
imap <C-Del> <C-O>dw

nnoremap <F5> :silent exec '!xfce4-terminal  -x python %' <CR><CR>
nnoremap <F6> :!py -2 %

nnoremap ,cd :cd %:p:h<CR>:pwd<CR>
nnoremap ,tn :tabnew<CR>
nnoremap ,tw :tab sp<CR>
nnoremap ,rw :res 10<CR>

nnoremap  :nohl<CR>
nnoremap <C-E> <C-E><C-E>
nnoremap <C-Y> <C-Y><C-Y>

let g:csv_delimiter = ";"

noremap ;; :%s:::g<Left><Left><Left>

"      \ *<C-R>=(expand("%:e")=="" ? "" : ".".expand("%:e"))<CR>
cabbrev lvim
      \ lvim /\<lt><C-R><C-W>\>/gj
      \ **
      \ <Bar> lw
      \ <C-Left><C-Left><C-Left><Right><Right>

cabbrev pss **\*.cpp **\*.c **\*.h **\*.hpp

cabbrev pcd <C-R>=fnameescape(expand("%:p:h"))<CR>
cabbrev prd <C-R>=fnameescape(expand("%:.:h"))<CR>

if has("gui_running")
    set background=light
else
    set background=dark
endif

if has("win32")
    set guifont=Courier_New:h12:cEASTEUROPE
else
    set guifont=Monospace\ 12
    nnoremap <S-Ins> "+p
    vnoremap <C-Ins> "+y
endif

