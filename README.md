Something cleaner can be done here, but for a fixed emissions curve this should work.

Installation process: 
1. create local environment 
```bash
# just on the first time do this
python3 -m venv .venv      # sets up the venv first time

# do this every time before starting the server
source .venv/bin/activate

# OR this if you use fish as a shell
source .venv/bin/activate.fish
```
2. Install required packages
```bash 
pip install -r requirements.txt
```

3. Run the file
```bash
python3 vesting_csv.py
```

Definitions:
- **token_quantity:** percentage of total distributed tokens
- **start_month:** month where tokens start to unlock
- **lock_period:** how long tokens are locked for
- **unlock_period:** `token_quantity / lock_period`
- lists with NULL values mean cliff month active

To-do:
- [x] convert txt to csv
- [x] chart the emissions schedule