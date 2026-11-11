FROM archlinux:base-devel

RUN pacman -Syu --noconfirm

RUN pacman -S --needed --noconfirm \
        rustup \
        vulkan-devel \
        vulkan-tools \
        wayland \
        libxkbcommon \
        xorgproto \
        libx11 \
        libxi \
        libxcursor \
        libxrandr \
        pkgconf \
        git \
        vim \
        less \
    && rustup default stable

WORKDIR /app

# Cache de dependências (projeto fantasma)
COPY Cargo.toml Cargo.lock* ./
RUN mkdir -p src \
    && echo "fn main() {}" > src/main.rs \
    && cargo build \
    && rm -rf src target/debug/deps/*