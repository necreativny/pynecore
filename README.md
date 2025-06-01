# fork
It's a fork where i'm running pynecore as python lib instead of running it with pyne cli, though i think that maybe script_runner.py can be refactored to be better siuted for such usage.(see script_runner.py)

Folder [demo](./demo/) is added, it shows how user's code would look like.

I don't know how people would want to use pynecore, right now we have cli and in this fork i show how would i like this library usage to look like. I think though, that separation of pynecore/core won't be bad anyways

# about myself
* i don't like syminfo... i just didn't enjoy seeing it...
* i don't undestand (python) oop( (ugh, go users)

# fakedocs
See examples in [demo](./demo/) folder.
Examples naming: <input_option>_<output_option>.py
* ohlcv_stdout.py -- simplest example, shows when you want to read data from ohlcv file but control the output
* csv_stdout.py -- example that shows how to use it with custom input and custom output. Shows how to create iterator to pass custom input data