# P5 Python Demos

Playing with this Python library: <https://github.com/p5py/p5>
Here are the docs: <https://p5.readthedocs.io/en/latest/#>

## Getting these up and running (macOS)

1. Clone the repository
2. Initialize `uv venv`
3. Ensure that you have the following packages installed via brew
    * glfw
    * libjpeg
    * freetype

> NOTE: The following may be necessary if Pillow fails to compile correctly:
>
> ``` bash
>  export LDFLAGS="-L/opt/homebrew/opt/jpeg/lib -L/opt/homebrew/opt/freetype/lib"
>  export CPPFLAGS="-I/opt/homebrew/opt/jpeg/include \
>                   -I/opt/homebrew/opt/freetype/include"
> ```

5. Run `uv install`
6. Run the any of the demos with `uv run ./demos/<demo_name>.py # Example: uv run ./demos/spiral.py`
