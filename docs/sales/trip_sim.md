# Trip simulation: what goes wrong at the door (auto-generated)

Real shops: 213 of 222 meal shops in our Tokyo areas have parseable hours (data/shops.json, checked Nov 2026).
Each simulated traveler: 10 sit-down meals over 5 Tokyo days, shop picked at random, arriving at a typical lunch or dinner time. 20,000 trips per group.
Group shares: JTA 2025 survey, US visitors. Meal times and "family = young kids" are assumptions.

## Careless traveler: picks a shop without checking hours

| group | share | turned away at least once in the trip | hits a rule Google Maps does not show at least once |
|---|---|---|---|
| solo | 33.7% | 98% | 100% |
| couple | 24.4% | 96% | 100% |
| friends | 18.1% | 99% | 100% |
| family with kids | 20.8% | 95% | 100% |

Per meal attempt (share of attempts where it happens):

| event | solo | couple | friends | family with kids |
|---|---|---|---|---|
| closed that weekday | 13.1% | 13.0% | 12.9% | 13.0% |
| closed at that hour (break or not open yet) | 15.2% | 12.4% | 19.8% | 11.3% |
| after last order | 2.5% | 1.8% | 3.6% | 0.6% |
| under 30 min to closing | 3.9% | 3.5% | 4.9% | 1.7% |
| credit cards not accepted | 41.5% | 41.2% | 41.3% | 41.4% |
| no young children | 0.0% | 0.0% | 0.0% | 1.5% |
| booking needed | 1.5% | 1.4% | 1.4% | 1.4% |
| cover / seat charge | 3.3% | 3.3% | 3.2% | 3.4% |

## Careful traveler: checks posted opening hours first (only goes to shops open at that time)

| group | turned away at least once (last order / children / booking) | meals out of 10 where credit cards are not accepted | arrives with under 30 min to closing at least once |
|---|---|---|---|
| solo | 43% | 3.8 | 46% |
| couple | 33% | 3.8 | 39% |
| friends | 56% | 3.7 | 56% |
| family with kids | 26% | 4.0 | 20% |

"Turned away" = closed that weekday, closed at that hour, after last order, children not accepted, or booking needed.
"Rule Google Maps does not show" = last order, under 30 min to closing, cash only, children, booking, cover charge.
Limits: random shop choice overstates closed-day misses for people who check hours first; rule flags exist only where our DB recorded them (house_rules on 68 shops), so hidden-rule rates are a floor.
