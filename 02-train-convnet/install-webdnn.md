git clone https://github.com/juj/emsdk.git
cd emsdk
./emsdk install sdk-incoming-64bit binaryen-master-64bit
./emsdk activate sdk-incoming-64bit binaryen-master-64bit

(see also http://webassembly.org/getting-started/developers-guide/ )

To enable em++ command, you need to type command on the shell.

source ./emsdk_env.sh

export CPLUS_INCLUDE_PATH=$PWD/eigen-eigen-67e894c6cd8f
