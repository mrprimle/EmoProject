
curl -O https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz &&
mkdir -p ffmpeg-release &&
tar Jxf ffmpeg-release-amd64-static.tar.xz --strip-components=1 -C ffmpeg-release &&
PATH=$(readlink -f ffmpeg-release):$PATH


