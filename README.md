# autotrack
📂 Update the trackers to add for qbittorrent

## Install
```BASH
git clone https://github.com/Neotoxic-off/autotrack
cd autotrack/autotrack
```

## Setup
- `qbittorrent.config` must be your qbittorrent config path

```JSON
{
    "flux": "https://raw.githubusercontent.com/ngosang/trackerslist/refs/heads/master/trackers_all.txt",
    "qbittorrent": {
        "config": "./test/config.conf",
        "section": "BitTorrent",
        "section_key": "Session\\AdditionalTrackers"
    }
}
```

## Run
```BASH
cd autotrack/autotrack
python3 autotrack
```
