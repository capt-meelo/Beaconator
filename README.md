# Beaconator
[![release](https://img.shields.io/github/release/capt-meelo/Beaconator?label=version&color=brightgreen)](https://github.com/capt-meelo/Beaconator/releases)
[![license](https://img.shields.io/github/license/capt-meelo/Beaconator?color=lightgrey)](https://github.com/capt-meelo/Beaconator/blob/main/LICENSE)
[![issues](https://img.shields.io/github/issues/capt-meelo/Beaconator?color=red)](https://github.com/capt-meelo/Beaconator/issues)
[![stars](https://img.shields.io/github/stars/capt-meelo/Beaconator)](https://github.com/capt-meelo/Beaconator/stargazers)
[![forks](https://img.shields.io/github/forks/capt-meelo/Beaconator?color=yellow)](https://github.com/capt-meelo/Beaconator/network)

Beaconator is an aggressor script for Cobalt Strike used to generate a raw **stageless** shellcode and packing the generated shellcode using [PEzor](https://github.com/phra/PEzor).


## How to Use
**Installing PEzor**

[PEzor](https://github.com/phra/PEzor) is required so install it first using the following:
```
git clone https://github.com/phra/PEzor.git
cd PEzor
./install.sh
```
> ***NOTE:** Make sure to add PEzor's `$PATH` variable in your `~/.profile` or `~/.bashrc` (if using Bash), **OR** `~/.zprofile` or `~/.zshrc` (if using ZSH).*


**Running Beaconator**

1. Load the `beaconator.cna` file via `Cobalt Strike > Script Manager`.
2. Access Beaconator from the menu bar.


## Screenshots

![options.png](./images/options.png "Pop Up Menu") 

![script-console.png](./images/script-console.png "Script Console Output") 


## Credits
- To **Francesco Soncina** ([@phraaaaaaa](https://twitter.com/phraaaaaaa)) for developing the awesome [PEzor](https://github.com/phra/PEzor).
