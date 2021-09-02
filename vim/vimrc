"set guifont=DroidSansMono\ Nerd\ Font\ Regular\ 14      
" set guifont=Sauce\ Code\ Pro\ Nerd\ Font\ Complete\ Mono\ Windows\ Compatible 14
" 设置字体

" 自动识别文件类型,使用文件类型plugin脚本,使用缩进定义文件
filetype indent plugin on
filetype on              " 设置开启文件类型侦测
set showcmd              " select模式下显示选中的行数
set ruler                " 总是显示光标位置
set cursorline           " 高亮显示当前行

filetype plugin on       " 设置加载对应文件类型的插件
" 打开语法加亮
syntax on
" session中不保存当前目录，这样使用Session.vim文件恢复时，Session.vim文件所在目录自动变成当前目录
set sessionoptions-=curdir
set sessionoptions+=sesdir
" 用啥鼠标
set mouse-=a
" 文件修改之后自动载入
set autoread
" 开启正则表达式的magic模式，例如使用\w匹配单词
set magic
" 设置不兼容vi, 只使用增强模式
set nocompatible
" 设置可以删除行首空格,断行, 进入Insert模式之前的位置
set backspace=indent,eol,start
" 新行使用设置自动缩进,使用上一行的缩进方式
set autoindent
" 设置智能缩进
set smartindent
" 设置命令历史列表的长度
set history=50
" 将TAB替换为空格
set expandtab
" 设置TAB宽度
set tabstop=4
" 和ignorecase配合实现智能大小写匹配
set smartcase
set ignorecase
" 在80个字符处设置锚线
set colorcolumn=110
" 补全内容不以分割子窗口形式出现，只显示补全列表
set completeopt=longest,menu,preview
" 使路径包含当前目录下的所有子目录
set path+=**
set langmenu=zh_CN.UTF-8
set helplang=cn
set termencoding=utf-8
set encoding=utf8
"set fileencodings=utf8
"set fileencodings=utf-8,ucs-bom,gbk,cp936,gb2312,gb18030
set fileencoding=chinese
set fileencodings=ucs-bom,utf-8,chinese
language message zh_CN.utf-8
set nu
" 打开文件自动定位到最后编辑的位置
autocmd BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | execute "normal! g'\"" | endif
" Make it so jk returns to normal mode
inoremap jk <esc>
" Python file settings ---------- {{{
augroup filetype_python
  autocmd!
  autocmd FileType python setlocal foldmethod=indent
  autocmd FileType python set foldlevel=99
" }}}


let mapleader = ";"
" 保存
nmap <leader>w :w<CR>
" 使用系统剪贴板
vmap <leader>y "+y
vmap <leader>d "+d
nmap <leader>p "+p
nmap <leader>P "+P

nnoremap <leader><leader>i :PlugInstall<cr>
nnoremap <leader><leader>u :PlugUpdate<cr>
nnoremap <leader><leader>c :PlugClean<cr>


" Easy editing/sourcing of vimrc
nnoremap <leader>ev :vsplit $MYVIMRC<cr>
nnoremap <leader>sv :source $MYVIMRC<cr>

" Useful shortcuts
nnoremap <leader>w :w<cr>
nnoremap <leader>q :q<cr>
nnoremap <leader><space> bi<space><esc>ea<space><esc>


" Specify a directory for plugins
call plug#begin('~/.vim/plugged')
" Include the following in the vim-plug section of your ~/.vimrc:

" Plug 'junegunn/vim-easy-align'

" Plug 'python-mode/python-mode', { 'for': 'python', 'branch': 'develop'  } 

"Miguel Grinberg
Plug 'preservim/nerdtree'   |  
            \ Plug 'tiagofumo/vim-nerdtree-syntax-highlight' |
            \ Plug 'Xuyuanp/nerdtree-git-plugin' |
            \ Plug 'ryanoasis/vim-devicons' |
            \ Plug 'jistr/vim-nerdtree-tabs' |
            \ Plug 'PhilRunninger/nerdtree-buffer-ops' |
"Plug 'pangloss/vim-javascript'
Plug 'joshdick/onedark.vim'
Plug 'vim-scripts/indentpython.vim'
" 能够显示当前文件各行的git状态
Plug 'airblade/vim-gitgutter'
Plug 'itchyny/lightline.vim'
Plug 'preservim/tagbar'
Plug 'lepture/vim-jinja'
Plug 'vim-syntastic/syntastic'
Plug 'ap/vim-buftabline'
Plug 'tpope/vim-sensible'

" Initialize plugin system
call plug#end()

"自动安装插件管理器
if empty(glob('~/.vim/autoload/plug.vim'))
    silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
                \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    augroup vim-plug_
        autocmd!
        autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
    augroup END
endif

" Set color scheme
colorscheme onedark

" nerdtree
nnoremap <silent> <leader>n :NERDTreeToggle<cr>
let g:NERDTreeDirArrowExpandable='|'
let g:NERDTreeDirArrowCollapsible='\'
" Plugin shortcutv
let g:NERDTreeDirArrow=1     "show node model
let g:NERDTreeHidden=0     "不显示隐藏文件
let g:NERDTreeMinimalUI=1     "不显示Help
nnoremap <c-n> :NERDTreeToggle<cr>
nnoremap <c-k> <c-w>k
nnoremap <c-j> <c-w>j
nnoremap <c-l> <c-w>l
nnoremap <c-h> <c-w>h


" nerdtree-git-plugin
let g:NERDTreeGitStatusIndicatorMapCustom = {
            \ "Modified"  : "✹",
            \ "Staged"    : "✚",
            \ "Untracked" : "✭",
            \ "Renamed"   : "➜",
            \ "Unmerged"  : "═",
            \ "Deleted"   : "✖",
            \ "Dirty"     : "✗",
            \ "Clean"     : "✔︎",
            \ 'Ignored'   : '☒',
            \ "Unknown"   : "?"
            \ }

" custom symbols
let g:NERDTreeGitStatusUseNerdFonts = 0 " you should install nerdfonts by yourself. default: 0
let g:NERDTreeGitStatusShowIgnored = 0 " a heavy feature may cost much more time. default: 0
let g:NERDTreeGitStatusUntrackedFilesMode = 'normal' " a heavy feature too. default: normal
let g:NERDTreeGitStatusConcealBrackets = 1 "How to show Clean indicator? default: 0
let g:NERDTreeGitStatusShowClean = 1 "How to hide the boring brackets([ ])? default: 0

