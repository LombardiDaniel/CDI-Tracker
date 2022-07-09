# CDI-Tracker

Simple CLI tool for using a script that tracks CDI x invested capital from a CSV file or public google sheet. Tested on MacOS and Linux (I don't know how installation would occur for Windows, I may do it later when I have more time).

Google Sheet must follow this format:

| Ammount Invested | Date of Transaction |
| ---------------- | ------------------- |
| 1000             | 22/08/2021          |
| 2000             | 03/02/2022          |
| 1300             | 11/05/2022          |
| ...              | ...                 |


#### Utilization:

After installation, run the command `cdi_track -h` for help. You can get the public URL of the Google Sheet by sharing it and then copying the given link. In case your sheetName is different than the default ('Sheet1'), you can pass it as an argument using the `--sheet_name` or `-n` flag.

If you prefer, you can just download it as a `.csv` file and pass it to the cli using the `-c` flag.

Usage Example:
```sh
cdi_track --url "httsp://MY_SHEET_URL"
cdi_track --csv "PATH_TO_CSV_FILE"
```

#### Download e uncompact:

```sh
wget -O CDI-Tracker.tar.gz https://github.com/LombardiDaniel/CDI-Tracker/archive/main.tar.gz && tar -xf CDI-Tracker.tar.gz
```

#### Install:

```sh
cd CDI-Tracker-main
make install
```

#### Uninstall:

(after navigating to the CDI-Tracker-main folder)

```sh
make uninstall
```
