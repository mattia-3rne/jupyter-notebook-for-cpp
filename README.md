# Jupyter Notebook für C++

C++-Code direkt in Jupyter-Zellen ausführen mit der Cell-Magic `%%cpp`.

## Voraussetzungen

- **g++** (GCC)
- **Python 3** mit pip

## Installation

```bash
pip install -r requirements.txt
```

## Nutzung

1. Jupyter starten und `template.ipynb` öffnen
2. Die Setup-Zelle ausführen
3. C++ in Zellen schreiben:

```cpp
%%cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

Optional: Compiler-Flags in der Magic-Zeile angeben, z. B. `%%cpp -std c++20`.
