Something cleaner can be done here, but for a fixed emissions curve this should work.

run `python3 vesting_csv.py`

Definitions:
- lists with NULL values mean cliff month active
- token_quantity: percentage of total distributed tokens
- start_month: month where tokens start to unlock
- lock_period: how long tokens are locked for
- unlock_period: `token_quantity / lock_period`

To-do:
- [x] convert txt to csv
- [ ] chart the emissions schedule