# go-crisp
A take home project for Go Crisp

### Running code and test suite provided through online code repo or in a tar-ball
Tests can be run if pytest is installed with `pytest` from the main directory.

This only requires pytest if run on Python3.11, which is what I used to test.

### Instructions on how to build and run the code with example data
Test_e2e.py shows how I'd recommend using this in a pipeline. You load a config file, verfiy the config file, then load data, then iterate through the rows and apply the transforms. Both good and bad rows are collected, though they could be discarded or passed to other systems as needed.

### Short architectural overview and technology choices made
This solution uses bare python, and only requires pytest for testing purposes. It evaluates each row individually, which is slow, but allows flexibility with error handling and would also allow transforms to reference other data within it's row.

This solution fits the requirements, though it's far from optimal. Things I don't like:
- using json to pass regex or transform config
- transforms are applied row wise, rather than column wise. if done by column, the problem space shrinks with each failed row; here, we apply transforms to a row until it fails, which is wasteful
- almost all of these transforms are easier to express in sql; duckdb would make this trivial, and sqlite would also be a acceptable solution
- it's single threaded, but since we're doing this row by row, it begs for a multithreaded approach.

### Documentation

Methods are laid out pretty clearly, with comments as to their function. None of the transforms are complex enough to require any significant explanation.

### List of assumptions or simplifications made
I went through some of these above, but in no particular order:
- This should be simple enough to read quickly (no multithreading)
- Should not use external libraries (duckdb, pandas, polars)
- data should be written out as csv (makes the transforms mostly worthless)
- On a large enough file, memory would be a issue (uses generator for ingest, allows checkpointing via append on write_csv method)

### List of the next steps you would want to do if this were a real project
- Finish tests for transforms 
- implement regex parsing of input columns (stubbed, didn't do)
- tear this all out and do it with sqlite
- fix todos noted in code