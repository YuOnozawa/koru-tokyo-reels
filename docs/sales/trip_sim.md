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
| closed that weekday | 13.0% | 12.9% | 12.9% | 13.0% |
| closed at that hour (break or not open yet) | 15.5% | 12.6% | 20.1% | 11.4% |
| after last order | 2.1% | 1.4% | 3.2% | 0.4% |
| under 30 min to closing | 4.0% | 3.6% | 5.0% | 1.7% |
| credit cards not accepted | 41.5% | 41.2% | 41.3% | 41.4% |
| no young children | 0.0% | 0.0% | 0.0% | 1.0% |
| booking needed | 1.0% | 1.0% | 0.9% | 0.9% |
| cover / seat charge | 2.8% | 2.8% | 2.8% | 2.9% |

## Careful traveler: checks posted opening hours first (only goes to shops open at that time)

| group | turned away at least once (last order / children / booking) | meals out of 10 where credit cards are not accepted | arrives with under 30 min to closing at least once |
|---|---|---|---|
| solo | 39% | 3.8 | 47% |
| couple | 29% | 3.8 | 40% |
| friends | 52% | 3.7 | 56% |
| family with kids | 20% | 4.0 | 20% |

"Turned away" = closed that weekday, closed at that hour, after last order, children not accepted, or booking needed.
"Rule Google Maps does not show" = last order, under 30 min to closing, cash only, children, booking, cover charge.
Limits: random shop choice overstates closed-day misses for people who check hours first; rule flags exist only where our DB recorded them (house_rules on 68 shops), so hidden-rule rates are a floor.
