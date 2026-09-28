import json
import random
import os

seed_path = os.path.join('server', 'db', 'seeds', 'seed-data.json')
with open(seed_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

rs_current = data.get('rs_current', [])
rs_full = data.get('rs_full', [])
all_mps = rs_current + rs_full

print(f"Loaded {len(all_mps)} total MPs.")

# Group MPs by state
mps_by_state = {}
for m in all_mps:
    st = m.get('state')
    if st:
        mps_by_state.setdefault(st, []).append(m)

print(f"Total states represented: {len(mps_by_state)}")

work_types = [
    'Road Construction', 'School Building', 'Water Supply',
    'Drainage System', 'Community Hall', 'Health Centre',
    'Bridge Construction', 'Street Lighting', 'Park Development',
    'Anganwadi Centre', 'Toilet Block', 'Solar Panel Installation'
]

statuses = ['Completed', 'In Progress', 'Tender Stage', 'Sanctioned', 'Stalled']
locations = [
    'Block A', 'Sector 4', 'Village Rampur', 'Ward 12', 'Panchayat Devpur',
    'NH Bypass', 'District HQ', 'GP Office', 'Nagar Palika Zone 3', 'Civil Hospital Area',
    'Model Town', 'Industrial Phase 1', 'Subdivision Complex', 'Taluk Centre'
]

random.seed(2026)

new_synthetic_works = []
wid = 1

for state, mps in sorted(mps_by_state.items()):
    # Determine how many MPs from this state to generate works for
    if len(mps) <= 2:
        selected_mps = mps
    elif len(mps) <= 5:
        selected_mps = mps[:3]
    elif len(mps) <= 15:
        selected_mps = mps[:5]
    else:
        selected_mps = mps[:8]

    # Generate 12 to 25 works per state
    works_per_mp = max(2, 16 // len(selected_mps))

    for mp in selected_mps:
        n_works = random.randint(works_per_mp, works_per_mp + 3)
        for _ in range(n_works):
            budget = random.randint(750000, 6500000)
            
            # Anomaly scenario probabilities
            scenario = random.choices(
                ['normal', 'cost_overrun', 'duplicate_work', 'rapid_full_payment', 'unverified_asset', 'stalled', 'no_progress'],
                weights=[0.40, 0.15, 0.08, 0.10, 0.12, 0.08, 0.07],
                k=1
            )[0]

            anomaly_type = None
            start_year = random.randint(2020, 2024)
            start_month = random.randint(1, 12)

            if scenario == 'cost_overrun':
                exp_pct = random.uniform(1.15, 1.45)
                comp_pct = random.randint(60, 100)
                status = 'Completed' if comp_pct >= 90 else 'In Progress'
                anomaly_type = 'cost_overrun'
            elif scenario == 'duplicate_work':
                exp_pct = random.uniform(0.3, 0.8)
                comp_pct = int(exp_pct * 100)
                status = 'In Progress'
                anomaly_type = 'duplicate_work'
            elif scenario == 'rapid_full_payment':
                exp_pct = random.uniform(0.85, 1.0)
                comp_pct = random.randint(5, 18)
                status = 'Sanctioned'
                anomaly_type = 'payment_before_progress'
            elif scenario == 'unverified_asset':
                exp_pct = random.uniform(0.9, 1.0)
                comp_pct = 100
                budget = max(budget, 3000000) # High-value >= 25L
                status = 'Completed'
                anomaly_type = 'unverified_high_value_asset'
            elif scenario == 'stalled':
                exp_pct = random.uniform(0.2, 0.6)
                comp_pct = random.randint(10, 45)
                status = 'Stalled'
                anomaly_type = 'stalled_work'
            elif scenario == 'no_progress':
                exp_pct = random.uniform(0.0, 0.1)
                comp_pct = 0
                start_year = min(start_year, 2022)
                status = 'Sanctioned'
                anomaly_type = 'no_progress'
            else:
                exp_pct = random.uniform(0.2, 0.95)
                comp_pct = min(100, int(exp_pct * 100) + random.randint(-5, 10))
                comp_pct = max(0, min(100, comp_pct))
                status = 'Completed' if comp_pct == 100 else ('In Progress' if comp_pct > 20 else 'Sanctioned')

            expenditure = int(budget * exp_pct)
            wtype = random.choice(work_types)
            loc = random.choice(locations)

            new_synthetic_works.append({
                'work_id': f'W{wid:04d}',
                'id': f'W{wid:04d}',
                'mp_id': mp['id'],
                'mp_name': mp.get('mp_name') or mp.get('name'),
                'state': state,
                'work_type': wtype,
                'work_name': f'{wtype} at {loc}',
                'sanctioned_amount': budget,
                'cost_estimate': budget,
                'expenditure': expenditure,
                'status': status,
                'start_year': start_year,
                'start_month': start_month,
                'completion_pct': comp_pct,
                'anomaly_type': anomaly_type
            })
            wid += 1

print(f"Generated {len(new_synthetic_works)} works across {len(mps_by_state)} states.")

# Verify all states have works
work_states = set(w['state'] for w in new_synthetic_works)
missing = set(mps_by_state.keys()) - work_states
print(f"States missing works: {missing}")

data['synthetic_works'] = new_synthetic_works
data['metadata']['works_count'] = len(new_synthetic_works)
data['metadata']['states'] = sorted(list(mps_by_state.keys()))

with open(seed_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Updated {seed_path} successfully.")

# Also update js/data.js for frontend standalone / fallback
data_js_path = os.path.join('js', 'data.js')
if os.path.exists(data_js_path):
    with open(data_js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Check if MPLADS_DATA is embedded in js/data.js
    if 'const MPLADS_DATA = ' in content:
        # replace it
        prefix = content.split('const MPLADS_DATA = ')[0] + 'const MPLADS_DATA = '
        suffix = ';\n' + content.split('const MPLADS_DATA = ')[1].split(';\n', 1)[1] if ';\n' in content.split('const MPLADS_DATA = ')[1] else ';\n'
        new_content = prefix + json.dumps(data, ensure_ascii=False, indent=2) + suffix
        with open(data_js_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {data_js_path} with new MPLADS_DATA.")
    else:
        print("Note: js/data.js uses ApiClient module.")
