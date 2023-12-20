# P5 Python Demos

Playing with this Python library: https://github.com/p5py/p5
Here are the docs: https://p5.readthedocs.io/en/latest/#

## Getting these up and running (macOS)

1. Clone the repository
2. Ensure that you have the following packagess installed via brew
`brew install glfw libjpeg`
3. Run the following command so that Pillow can compile corretly:
``` bash
  export LDFLAGS="-L/opt/homebrew/opt/jpeg/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/jpeg/include"
```
4. Now install everything using pipen `pipenv install --dev`
5. Run the spiral demo with `pipenv run python ./spiral.py``
