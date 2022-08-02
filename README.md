# Debug.LogError() Finder
A simple Python script to find all occurrences of `Debug.LogError()` in all the `.cs` files located in a given directory.

## Background 
[Debug.LogError()](https://docs.unity3d.com/ScriptReference/Debug.LogError.html) is a useful Unity scripting API function, that allows a developer to log an error message to the console. 

As a result, these calls are often left in the code of various games and applications that make use of Unity. This tool aims to make it easier to find these calls, such as when looking for debug strings to document on [The Cutting Room Floor](https://tcrf.net/).

## Usage
Run the script using your Python environment of choice:

```
python main.py
```

When providing the directory path, ensure that you provide an un-escaped directory (i.e. `D:\path\to\files` rather than `D:\\path\\to\\files`)

## License
[Unlicense](https://choosealicense.com/licenses/unlicense/)
