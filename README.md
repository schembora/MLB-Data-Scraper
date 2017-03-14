# MLBDataScraper
Python scraper of the MLB Database

## Usage:


```python
from bs4 import BeautifulSoup
from mlbdatascraper import MLBData

dayObj = MLBData('DD/MM/YYYY')

gameObj = dayObj.getTeamData('teamAbbrv')
```
## Examples:
```python
gameObj.linescore.hr.away
```
returns number of homeruns scored by away team
```python
gameObj.homeruns
```
returns array of objects with properties std_hr, hr, id, last, team_code, inning, runners, number, name_display_roster, first
```python
players = gameObj.homeruns
for player in players:
  player.runners
```
returns the number of players on base when the player hit the homerun, for each player

## Properties:
away_code

away_division

away_file_code

away_games_back

away_games_back_wildcard

away_league_id

away_loss

away_name_abbrev

away_sport_code

away_team_city

away_team_id

away_team_name

away_time

away_time_zone

away_win

broadcast

count

day

description

double_header_sw

first_pitch_et

game_data_directory

game_medial

game_nbr

game_pk

game_type

gameday

gameday_sw

hm_lg_ampm

home_ampm

home_code

home_division

home_file_code

home_games_back

home_games_back_wildcard

home_league_id

home_loss

home_name_abbrev

home_runs

	[std_hr hr id last team_code inning runners number name_display_roster first, ...]

home_sport_code

home_team_city

home_team_id

home_team_name

home_time

home_time_zone

home_win

id

index

league

linescore

	hr

		home

		away

	e

		home

		away

	so

		home

		away

	r

		home

		away

	sb

		home

		away

	inning

		[home away, home away, ...]

	h

		home

		away

links

location

losing_pitcher

	id

	last

	losses

	era

	number

	name_display_roster

	first

	wins

original_date

resume_date

save_pitcher

	id

	last

	saves

	loses

	era

	name_display_roster

	number

	svo

	first

	wins

scheduled_innings

status

	is_no_hitter

	top_inning

	s

	b

	reason

	ind

	status

	is_perfect_game

	o

	inning

	inning_state

	note

tbd_flag

tiebreaker_sw

time

time_aw_lg

time_date

time_date_aw_lg

time_date_hm_lg

time_hm_lg

time_zone

time_zone_aw_lg

time_zone_hm_lg

tz_aw_lg_gen

tz_hm_lg_gen

venue

venue_id

venue_w_chan_loc

video_thumbnail

video_thumbnails

winning_pitcher

	id

	last

	losses

	era

	number

	name_display_roster

	first

	wins

	
