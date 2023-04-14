# ETH_Explorer
GUI built using python to explore Ethereum blockchain

### Working with virtual environment of Linux (Raspberry-Pi)
To activate: `$ source venv/bin/activate`<br>
To Decativate: `decativate`

### Reading data from .env file
Library required: `pip install python-decouple`

**Write data on `.env` file**<br>
API_KEY=hhsaherinrefh123344

**Read .env variables in Python**
```python
from decouple import config
KEY = config('API_KEY')
print(KEY)
```

# Troubleshooting

## Error while installing web3 library on windows: pip install web3

- Install Visual Studio Build Tools [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- Select the C++ Desktop development Workload for installation (should include "Visual C++ Build tools core features", "MSVC toolset C++ 2019 v142 (x86,x64)", "Visual C++ 2019 Redistributable Update" and "Windows 10 SDK (10.0.17763.0) for Desktop C++")
- Finish installation and reboot laptop
- Open Visual Studio Code and retry pip install web3
