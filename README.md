# P5 Python Demos

Playing with this Python library: https://github.com/p5py/p5
Here are the docs: https://p5.readthedocs.io/en/latest/#

## Getting these up and running (macOS)

1. Clone the repository
2. Ensure that you have the following packagess installed via brew
`brew install glfw libjpeg freetype`
3. Start a pipenv shell `pipenv shell`
4. Run the following command so that Pillow can compile corretly:
``` bash
  export LDFLAGS="-L/opt/homebrew/opt/jpeg/lib -L/opt/homebrew/opt/freetype/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/jpeg/include -I/opt/homebrew/opt/freetype/include"
```
5. Now run the install for p5 `pip install p5` (it has to be done like this due to building Pillow)
6. Now install everything else using pipenv `pipenv install --dev`
7. Run the spiral demo with `python ./spiral.py``